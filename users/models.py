from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

class CustomUser(AbstractUser):
  
  def __str__(self):
    return self.username

class Profile(models.Model):
  phone_number = models.CharField(max_length=12, blank=True, null=True)
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='profile')
