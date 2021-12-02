from rest_framework.serializers import ModelSerializer

from .models import *


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['likes'] = instance.likes.filter(value='like').count()
    #                               # - instance.likes.filter(value='dislike').count()

