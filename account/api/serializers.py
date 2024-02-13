from rest_framework import serializers
from account.models import CustomUser, Profile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'avatar']



class CustomUserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'crimesection_admin', 'entertainment_admin', 'phone', 'password1', 'password2']

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match.")

        password = attrs['password1']

        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)

        return attrs

    def create(self, validated_data):
        # Remove password fields from validated data
        password = validated_data.pop('password1')
        validated_data.pop('password2')

        # Create user without password
        user = CustomUser.objects.create(**validated_data)

        # Set password separately
        user.set_password(password)
        user.save()

        return user


class CustomUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'crimesection_admin', 'entertainment_admin', 'phone', 'is_active', 'is_staff', 'profile']

