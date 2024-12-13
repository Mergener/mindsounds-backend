from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PasswordResetView, SetNewPasswordView

urlpatterns = [
    path('reset-password/', PasswordResetView.as_view(), name='password_reset'),
    path('confirm-reset-password/', SetNewPasswordView.as_view(), name='password_reset_confirm'),
]