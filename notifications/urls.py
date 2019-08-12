from django.conf.urls import url
from .views import sms_response

urlpatterns = [
  url(r'^$', sms_response, name='sms')
  ]
