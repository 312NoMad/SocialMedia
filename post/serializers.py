from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *


class PostSerializer(ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('article', 'text', 'author')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['rating'] = instance.likes.filter(value='like').count() - instance.likes.filter(value='dislike').count()
        return representation


class PostDetailsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)

    def validate_like(self, post):
        request = self.context.get('request')
        user = request.user
        if self.Meta.model.objects.filter(post=post,
                                          user=user).exists():
            raise serializers.ValidationError('Вы уже оставляли лайк')
        return post
