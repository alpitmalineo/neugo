from django.contrib import admin

from api.models import City, BusAvailability, SeatsAvailability, PreferSeatRow

# Register your models here.
admin.site.register(City)
admin.site.register(BusAvailability)
admin.site.register(SeatsAvailability)
admin.site.register(PreferSeatRow)

