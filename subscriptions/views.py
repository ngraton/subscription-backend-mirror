from rest_framework.viewsets import ModelViewSet
from rest_framework
from .serializers import SubscriptionSerializer
from .models import Subscription

class SubscriptionViewSet(ModelViewSet):
  serializer_class = SubscriptionSerializer
  queryset = Subscription.objects.all()
  filter_backends =
  
  # def get_queryset(self):
  #       user = self.request.user
  #       return Subscription.objects.filter(user=user)
