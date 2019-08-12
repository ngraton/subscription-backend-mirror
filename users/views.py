from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import generics, viewsets
from .serializers import CustomUserSerializer, ProfileSerializer
from .models import CustomUser, Profile

class CustomUserListView(viewsets.ModelViewSet):
  serializer_class = CustomUserSerializer
  queryset = CustomUser.objects.all()
  filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
  filterset_fields = ['username']

class ProfileViewSet(viewsets.ModelViewSet):
  serializer_class = ProfileSerializer
  queryset = Profile.objects.all()
