from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

class CustomUser(AbstractUser):
  phone_number = models.CharField(max_length=12, blank=True, null=True)
  
  def __str__(self):
    return self.username
