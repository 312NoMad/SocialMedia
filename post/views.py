from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import *
from .permissions import IsAuthorOrAdmin
from .serializers import *


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'update', 'partial_update', 'destroy', 'create']:
            return PostSerializer
        if self.action == 'retrieve':
            return PostDetailsSerializer
        return []

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAuthorOrAdmin()]
        return []


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action == 'destroy':
            return [IsAuthorOrAdmin(), IsAuthenticated()]
        return [IsAuthenticated()]




