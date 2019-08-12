from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from .api import router
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^sms/', include('notifications.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    
]
