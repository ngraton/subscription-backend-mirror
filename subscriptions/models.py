from django.db import models

class Subscription(models.Model):
  INTERVALS =  [
    ('annual', 'Annual'),
    # ('Semiannual', 'Semiannual')
    ('quarterly', 'Quarterly'),
    ('monthly', 'Monthly'),
    # ('Weekly', 'Weekly')
]

  name = models.CharField()
  due_date = models.DateField()
  payment = models.DecimalField()
  interval = models.CharField(max_length=10,
        choices=INTERVALS)
  user = models.ForeignKey('CustomUser', related_name='subscriptions', on_delete=models.CASCADE)

