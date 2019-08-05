from rest_framework.serializers import ModelSerializer

from .models import CustomUser

class CustomUserSerializer(ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('username', 'id', 'subscriptions')
    depth=1