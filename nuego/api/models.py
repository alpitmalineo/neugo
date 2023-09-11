from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models
from accounts.models import TimeAt


# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class BusAvailability(TimeAt):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coach = models.CharField(max_length=70)
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city', null=True)
    destination_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination_city', null=True)
    date = models.DateField()
    hours = models.CharField(max_length=30)
    boarding_point = models.CharField(max_length=80)
    dropping_point = models.CharField(max_length=80)
    departure_time = models.TimeField()
    destination_time = models.TimeField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.coach)


class SeatsAvailability(TimeAt):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    bus = models.ForeignKey(BusAvailability, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.bus)


PREFER_ROW_CHOICES = (
    ('Front', 'Front'),
    ('Center', 'Center'),
    ('Back', 'Back'),
)

PREFER_SEAT_CHOICES = (
    ('Window', 'Window'),
    ('Aisle', 'Aisle'),
)


class PreferSeatRow(TimeAt):
    prefer_row = models.CharField(max_length=10, choices=PREFER_ROW_CHOICES)
    prefer_seat = models.CharField(max_length=10, choices=PREFER_SEAT_CHOICES)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)
    seat = models.ForeignKey(SeatsAvailability, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.seat, self.prefer_row, self.prefer_seat, self.seat_number)
