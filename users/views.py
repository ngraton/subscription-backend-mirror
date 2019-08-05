from django.shortcuts import render
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomUserViewSet(ModelViewSet):
  serializer_class = CustomUserSerializer
  queryset = CustomUser.objects.all()
  filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
  filterset_fields = ['username']

