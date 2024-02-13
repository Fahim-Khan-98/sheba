from django.urls import path
from .views import CustomUserListCreateAPIView, CustomUserRetrieveUpdateAPIView,\
    ProfileListCreateAPIView, ProfileRetrieveUpdateAPIView, GetRoutes, LogoutAPIView
from rest_framework.authtoken import views

urlpatterns = [
    path('', GetRoutes.as_view(), name='get-route'),
    path('api/v1/users/', CustomUserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/v1/users/<int:pk>/', CustomUserRetrieveUpdateAPIView.as_view(), name='user-detail'),
    path('api/v1/profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('api/v1/profiles/<int:pk>/', ProfileRetrieveUpdateAPIView.as_view(), name='profile-detail'),
    
    # authentication
    path('login/', views.obtain_auth_token, name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
]
