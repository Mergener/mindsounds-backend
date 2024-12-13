from django.urls import path
from .views import PostDetailView, PostListCreateView, FeedView, UserPostsView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('user/<int:pk>/', UserPostsView.as_view(), name='user-posts'),
]