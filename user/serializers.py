from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import status

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User

        fields = ['id', 'email', 'name', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    id = serializers.ReadOnlyField()

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(status.HTTP_400_BAD_REQUEST)

        if password is None:
            raise serializers.ValidationError(status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            raise serializers.ValidationError(status.HTTP_400_BAD_REQUEST)

        return {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'token': user.token,
        }