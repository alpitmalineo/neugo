from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.filters import BusAvailabilityFilter, SeatAvailabilityFilter
from api.models import BusAvailability, SeatsAvailability, PreferSeatRow
from api.serializers import (BusAvailabilitySerializer, SeatsBookingSerializer,
                             GetBookSeatsSerializer, GetBusPreferSeatRowSerializer,
                             PreferSeatRowSerializer, GetPreferSeatRowSerializer)


# Create your views here.
class BusAvailabilityView(generics.ListAPIView):
    serializer_class = BusAvailabilitySerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = BusAvailabilityFilter
    filterset_fields = ['departure_city', 'destination_city', 'date',
                        'boarding_point', 'dropping_point']
    queryset = BusAvailability.objects.all().select_related('user', 'departure_city',
                                                            'destination_city')


class SeatAvailability(generics.ListAPIView):
    queryset = PreferSeatRow.objects.filter(is_booked=False).select_related('seat__bus__departure_city',
                                                                            'seat__bus__destination_city')
    permission_classes = (AllowAny,)
    serializer_class = PreferSeatRowSerializer
    filterset_class = SeatAvailabilityFilter

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetBusPreferSeatRowSerializer
        else:
            return PreferSeatRowSerializer

    def post(self, request, format=None):
        try:
            coach = request.data.get("coach")
            prefer_row = request.data.get("prefer_row")
            prefer_seat = request.data.get("prefer_seat")
            total_pax = int(request.data.get("total_pax", 1))

            # import pdb;pdb.set_trace()
            seats = PreferSeatRow.objects.filter(seat__bus__coach=coach, prefer_row=prefer_row,
                                                 prefer_seat=prefer_seat, is_booked=False)

            if len(seats) < total_pax or total_pax > 2:
                return Response({"message": f"Not enough available seats for {total_pax} passengers."},
                                status=status.HTTP_400_BAD_REQUEST)

            selected_seats = seats[:total_pax]

            if selected_seats:
                serializer = GetBusPreferSeatRowSerializer(seats, many=True)
                return Response(serializer.data)
            else:
                return Response({"message": "Seats not available for selected combination. Please revise your inputs."},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BookSeatView(generics.ListCreateAPIView):
    queryset = SeatsAvailability.objects.all()[2::].select_related('user', 'bus__departure_city',
                                                              'bus__destination_city').prefetch_related(
        'preferseatrow_set')

    serializer_class = SeatsBookingSerializer
    # permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetBookSeatsSerializer
        else:
            return SeatsBookingSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'Seats Booked Successfully !'}, status=status.HTTP_201_CREATED)

    # def create(self, request):
    #     serializer = SeatsBookingSerializer(data=request.data)
    #     if serializer.is_valid():
    #         seat_bookings = serializer.validated_data['seat_bookings']
    #         for seat_booking_data in seat_bookings:
    #             SeatsAvailability.objects.create(**seat_booking_data)
    #         return Response({'message': 'Seats booked successfully'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
