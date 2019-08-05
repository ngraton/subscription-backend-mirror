from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomUserViewSet(ModelViewSet):
  serializer_class = CustomUserSerializer
  queryset = CustomUser.objects.all()
  


