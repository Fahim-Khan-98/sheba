from django.urls import path
from .views import CustomUserListCreateAPIView, CustomUserRetrieveUpdateDestroyAPIView
# , ProfileListCreateAPIView, ProfileRetrieveUpdateDestroyAPIView
from rest_framework.authtoken import views

urlpatterns = [
    path('users/', CustomUserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    # path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    # path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-detail'),
    path('api-token-auth/', views.obtain_auth_token),
]
