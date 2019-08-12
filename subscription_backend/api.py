from rest_framework.routers import DefaultRouter

from subscriptions.views import SubscriptionViewSet
from users.views import ProfileViewSet, CustomUserListView

router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet)
router.register('profile', ProfileViewSet)
router.register('users', CustomUserListView)
