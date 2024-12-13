from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import Profile, Follower
from .serializers import ProfileSerializer, FollowerSerializer, ProfilePictureSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User

class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise permissions.PermissionDenied("Profiles are created automatically.")

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class ProfileByUserNameView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_name):
        user = User.objects.get(username=user_name)
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

class FollowUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user = request.user
        follow_user = User.objects.get(id=user_id)
        Follower.objects.create(user=follow_user, follower=user)
        return Response({"message": f"You are now following {follow_user.username}"})

class UnfollowUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user = request.user
        follow_user = User.objects.get(id=user_id)
        Follower.objects.filter(user=follow_user, follower=user).delete()
        return Response({"message": f"You are no longer following {follow_user.username}"})

class FollowersView(generics.ListAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = User.objects.get(id=self.kwargs['user_id'])
        return Follower.objects.filter(user=user)

class FollowingView(generics.ListAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = User.objects.get(id=self.kwargs['user_id'])
        return Follower.objects.filter(follower=user)

class FollowersCountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        followers_count = Follower.objects.filter(user=user).count()
        return Response({"followers_count": followers_count})

class FollowingCountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        following_count = Follower.objects.filter(follower=user).count()
        return Response({"following_count": following_count})

class IsFollowingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        user = request.user
        follow_user = User.objects.get(id=user_id)
        is_following = Follower.objects.filter(user=follow_user, follower=user).exists()
        return Response({"is_following": is_following})

class ProfilePictureUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        profile = request.user.profile 
        serializer = ProfilePictureSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile picture uploaded successfully!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '')  
        query = query.strip().split('/')[0]
        if query:
            users = User.objects.filter(username__icontains=query)  
        else:
            users = User.objects.none()  

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)