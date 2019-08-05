from rest_framework.routers import DefaultRouter

from subscriptions.views import SubscriptionViewSet
from users.views import CustomUserViewSet

router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet)
router.register('users', CustomUserViewSet)