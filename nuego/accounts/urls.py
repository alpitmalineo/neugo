from django.urls import path

from accounts import views

urlpatterns = [
    # User Register
    path('register/', views.UserCreateView.as_view(), name="user-register"),

    # User Login
    path('login/', views.UserLoginView.as_view(), name="user-login"),
]
