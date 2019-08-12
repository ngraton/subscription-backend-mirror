from django.db import models
from users.models import CustomUser

class Notification(models.Model):
  phone_number = models.CharField(max_length=12)
  user = models.ForeignKey(
    CustomUser,
    related_name='subscriptions', 
    on_delete=models.CASCADE)
  message = models.CharField(max_length=200)
  time_stamp = models.DateTimeField(auto_now_add=True)
