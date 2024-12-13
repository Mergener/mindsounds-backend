# Profiles serializers.py

from rest_framework import serializers
from .models import Profile, Follower
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(use_url=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'profile_picture', 'username']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'profile']

class FollowerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    follower = UserSerializer()

    class Meta:
        model = Follower
        fields = '__all__'

class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_picture']