from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.serializers import UserSerializer
from api.models import City, BusAvailability, SeatsAvailability, PreferSeatRow
from api.utils import is_seat_booked


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city',)


class BusAvailabilitySerializer(serializers.ModelSerializer):
    departure_city = CitySerializer(read_only=True)
    destination_city = CitySerializer(read_only=True)

    class Meta:
        model = BusAvailability
        fields = ('id', 'coach', 'departure_city', 'destination_city', 'date',
                  'hours', 'boarding_point', 'dropping_point', 'departure_time',
                  'destination_time', 'price')


class PreferSeatRowSerializer(serializers.ModelSerializer):
    total_pax = serializers.IntegerField()
    # coach = serializers.CharField(required=False)
    # coach = serializers.PrimaryKeyRelatedField(queryset=BusAvailability.objects.all())
    coach = serializers.SlugRelatedField(slug_field='coach', queryset=BusAvailability.objects.all())

    class Meta:
        model = PreferSeatRow
        fields = ('coach', 'prefer_row', 'prefer_seat', 'total_pax')


class SeatsAvailabilitySerializer(serializers.ModelSerializer):
    bus = BusAvailabilitySerializer(read_only=True)

    class Meta:
        model = SeatsAvailability
        fields = ('bus',)


class GetBusPreferSeatRowSerializer(serializers.ModelSerializer):
    seat = SeatsAvailabilitySerializer(read_only=True)

    class Meta:
        model = PreferSeatRow
        fields = ('seat', 'prefer_row', 'prefer_seat', 'seat_number', 'is_booked', 'created_at', 'updated_at')
        read_only_fields = ('seat', 'is_booked', 'created_at', 'updated_at')


class GetPreferSeatRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferSeatRow
        fields = ('prefer_row', 'prefer_seat', 'seat_number', 'is_booked', 'created_at', 'updated_at')
        read_only_fields = ('is_booked', 'created_at', 'updated_at')


class GetBookSeatsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    bus = BusAvailabilitySerializer(read_only=True)
    seat = GetPreferSeatRowSerializer(read_only=True, many=True, source="preferseatrow_set")
    total_passengers = serializers.SerializerMethodField()

    class Meta:
        model = SeatsAvailability
        fields = ('id', 'user', 'bus', 'seat', 'total_passengers', 'created_at', 'updated_at')

    def get_total_passengers(self, obj):
        seat_data = obj.preferseatrow_set.all()
        total_passengers = len(seat_data)
        return total_passengers


class SeatsBookingSerializer(serializers.ModelSerializer):
    """ Seat booking Create"""
    seat = GetPreferSeatRowSerializer(write_only=True, required=False, many=True)

    class Meta:
        model = SeatsAvailability
        fields = ('bus', 'seat')

    def create(self, validated_data):
        # import pdb;pdb.set_trace()
        seats = validated_data.pop('seat')
        for seat_preference_data in seats:
            prefer_row = seat_preference_data["prefer_row"]
            prefer_seat = seat_preference_data["prefer_seat"]
            seat_number = seat_preference_data["seat_number"]
            if PreferSeatRow.objects.filter(prefer_row=prefer_row, prefer_seat=prefer_seat, seat_number=seat_number,
                                            is_booked=True).exists():
                raise ValidationError("Seats already booked by other.")
            # import pdb;pdb.set_trace()
            is_booked = is_seat_booked(seats)
            if is_booked is False:
                raise ValidationError("Seats not available for selected combination. Please revise your inputs.")
            else:
                instance = SeatsAvailability.objects.create(**validated_data)

                array = []
                for dic in seats:
                    # prefer_seat_row = PreferSeatRow.objects.create(**dic)
                    array.append(PreferSeatRow(**dic, seat=instance, is_booked=True))
                PreferSeatRow.objects.bulk_create(array)
                return instance

    # class BulkSeatsAvailabilitySerializer(serializers.Serializer):
    #     seat_bookings = SeatsAvailabilitySerializer(many=True)

    # def create(self, validated_data):
    #     print(validated_data, "-----------------")
    #     # seat = validated_data.get('seat')
    #     # import pdb;pdb.set_trace()
    #     array = []
    #     instance = SeatsAvailability.objects.create(**validated_data)
    #     for dic in validated_data:
    #
    #
    #         array.append(SeatsAvailability(**dic, seat=instance))
    #     SeatsAvailability.objects.bulk_create(array)
    #     return instance
    #     # from_city = validated_data.pop('from_city')
    #     # to_city = validated_data.pop('to_city')
    #     # city_f = CityCountry.objects.create(**from_city)
    #     # city_t = CityCountry.objects.create(**to_city)
    #     # place = validated_data.pop('place')
    #     #
    #     # instance = SeatsAvailability.objects.create(from_city=city_f, to_city=city_t, **validated_data)
    #     # array = []
    #     # for dic in place:
    #     #     array.append(Place(**dic, trip=instance))
    #     # Place.objects.bulk_create(array)
    #     # return instance
