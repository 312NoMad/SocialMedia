from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    pass


class ActivationSerializer(serializers.Serializer):
    pass


class LoginSerializer(serializers.Serializer):
    pass