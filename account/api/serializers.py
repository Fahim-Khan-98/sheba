from rest_framework import serializers
from account.models import CustomUser, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'avatar']



class CustomUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'crimesection_admin', 'entertainment_admin', 'phone', 'is_active', 'is_staff']

        

class CustomUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'crimesection_admin', 'entertainment_admin', 'phone', 'is_active', 'is_staff', 'profile']

