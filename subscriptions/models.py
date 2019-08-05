from django.db import models
from users.models import CustomUser

class Subscription(models.Model):
  INTERVALS =  [
    ('annual', 'annual'),
    # ('Semiannual', 'Semiannual')
    ('quarterly', 'quarterly'),
    ('monthly', 'monthly'),
    # ('Weekly', 'Weekly')
]

  name = models.CharField(max_length=200)
  due_date = models.DateField()
  payment = models.IntegerField()
  interval = models.CharField(max_length=10,
        choices=INTERVALS)
  user = models.ForeignKey(CustomUser, related_name='subscriptions', on_delete=models.CASCADE)

