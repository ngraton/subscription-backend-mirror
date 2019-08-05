from rest_framework.viewsets import ModelViewSet
from .serializers import SubscriptionSerializer
from .models import Subscription

class SubscriptionViewSet(ModelViewSet):
  serializer_class = SubscriptionSerializer
  queryset = Subscription.objects.all()
  
  # def get_queryset(self):
  #       user = self.request.user
  #       return Subscription.objects.filter(user=user)
