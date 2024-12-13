from django.urls import path
from .views import ProfilePictureUploadView, ProfileDetailView, ProfileListCreateView, FollowersView, FollowingView, UnfollowUser, FollowUser, FollowersCountView, ProfileByUserNameView, FollowingCountView, IsFollowingView, UserSearchView

urlpatterns = [
    path('', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('<int:user_id>/followers/', FollowersView.as_view(), name='followers'),
    path('<int:user_id>/following/', FollowingView.as_view(), name='following'),
    path('<int:user_id>/follow/', FollowUser.as_view(), name='follow'),
    path('<int:user_id>/unfollow/', UnfollowUser.as_view(), name='unfollow'),
    path('<int:user_id>/followers-count/', FollowersCountView.as_view(), name='followers-count'),
    path('<int:user_id>/following-count/', FollowingCountView.as_view(), name='following-count'),
    path('is-following/<int:user_id>/', IsFollowingView.as_view(), name='is-following'),
    path('upload-profile-picture/', ProfilePictureUploadView.as_view(), name='upload_profile_picture'),
    path('by-username/<str:user_name>/', ProfileByUserNameView.as_view(), name='profile-by-username'),
    path('search/', UserSearchView.as_view(), name='search-users'),
]