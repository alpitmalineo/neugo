from django.contrib.auth.models import update_last_login
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from accounts.models import User
from accounts.serializers import UserLoginSerializer, UserSerializer, UserCreateSerializer
from rest_framework import filters


# Create your views here.

class UserCreateView(generics.CreateAPIView):
    """This view endpoint for User create"""
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]

    def get_queryset(self):
        return User.objects.all()

        # def get_serializer_class(self):
        #     if self.request.method == "GET":
        #         return UserSerializer
        #     else:
        #         return UserCreateSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    """This view endpoint for login"""
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            print(serializer.data)
            email = serializer.data['email']
            user = User.objects.get(email=email)
            if user.check_password(serializer.data['password']) is False:
                error = {'password': ["Password is wrong", ]}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
            elif not user.is_active:
                error = {'email': ["This user account is disabled.", ]}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
            else:
                update_last_login(None, user)
                data = UserSerializer(user, context={"request": self.request}).data
                return Response(data, status=status.HTTP_200_OK)
        except User.DoesNotExist as e:
            error = {'email': ["This email is not valid", ]}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
