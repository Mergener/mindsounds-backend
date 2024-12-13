# Serializers
from rest_framework import serializers
from .models import Post
from profiles.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    class Meta:
        model = Post
        fields = ['id', 'created_at', 'updated_at', 'author', 'content']
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']