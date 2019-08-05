from django.contrib import admin
from django.conf.urls import url, include
from .api import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^token-auth/', views.obtain_auth_token),
    url(r'^api/', include(router.urls)),
]