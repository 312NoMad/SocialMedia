from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import *


class Registration(APIView):

    def post(self, request):
        serializer = RegistrationSerializer
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response('Аккаунт успешно зарегистрирован', status=201)


class Activation(APIView):

    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activated()
            return Response('Аккаунт успешно активирован', status=200)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно разлогинились')
