from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomUserListView(generics.ListAPIView):
  serializer_class = CustomUserSerializer
  queryset = CustomUser.objects.all()
  filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
  filterset_fields = ['username',]

