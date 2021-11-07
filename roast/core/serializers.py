from django.db import models
from rest_framework import serializers
from core.models import UserProfile
from authentication.models import User


class UserSerializer (serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserRegisteration(serializers.ModelSerializer):

    profile = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email','password','profile')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            first_name = profile_data['first_name'],
            last_name = profile_data['last_name'],
            phone_number = profile_data['phone_number'],
            profile_pic = profile_data['profile_pic'],
            age = profile_data['age'],
            gender = profile_data['gender'],
            level = profile_data['level'],
            bio = profile_data['bio']
        )
        return user

        