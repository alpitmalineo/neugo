from django.urls import path

from api import views

urlpatterns = [
    # Bus Availability
    path('bus_availability/', views.BusAvailabilityView.as_view(), name="bus-availability"),

    # User Login
    path('book_seat/', views.BookSeatView.as_view(), name="book-seat"),
    path('seat/', views.SeatAvailability.as_view(), name="seat"),
]
