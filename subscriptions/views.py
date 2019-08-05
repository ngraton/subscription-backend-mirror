from rest_framework.viewsets import ModelViewSet
from .serializers import SubscriptionSerializer
from .models import Subscription

class SubscriptionViewSet(ModelViewSet):
  serializer_class = SubscriptionSerializer
  queryset = Subscription.objects.all()
  # def get_queryset(self):
  #       """
  #       This view should return a list of all the purchases
  #       for the currently authenticated user.
  #       """
  #       user = self.request.user
  #       return Subscriptions.objects.filter(user=user)
