from rest_framework.serializers import ModelSerializer

from .models import CustomUser, Profile

class CustomUserSerializer(ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('username', 'subscriptions', 'id', 'profile')
    depth = 1

class ProfileSerializer(ModelSerializer):
  class Meta:
    model = Profile
    fields = ('phone_number', 'user')
