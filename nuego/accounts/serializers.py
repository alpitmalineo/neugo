from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """Users login after can see this credentials"""

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'is_active')
        read_only_fields = ('id', 'email', 'name', 'is_active',)


class UserCreateSerializer(serializers.ModelSerializer):
    """This serializer for site users registration"""
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True,
                                     required=True, validators=[validate_password, ])

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'is_active')

        extra_kwargs = {
            'password': {'write_only': True},

        }
        read_only_fields = ('is_active',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            return value
        else:
            raise serializers.ValidationError("This User Doesn't exist!")
