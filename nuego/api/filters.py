import django_filters
from .models import BusAvailability, PreferSeatRow


class BusAvailabilityFilter(django_filters.FilterSet):
    departure_time__gte = django_filters.TimeFilter(field_name='departure_time', lookup_expr='gte')
    departure_time__lte = django_filters.TimeFilter(field_name='departure_time', lookup_expr='lte')

    class Meta:
        model = BusAvailability
        fields = ['departure_city', 'destination_city', 'date', 'boarding_point', 'dropping_point']


class SeatAvailabilityFilter(django_filters.FilterSet):
    coach = django_filters.ModelChoiceFilter(field_name="seat__bus__coach", queryset=BusAvailability.objects.all())

    class Meta:
        model = PreferSeatRow
        fields = ['coach', 'prefer_row', 'prefer_seat']
