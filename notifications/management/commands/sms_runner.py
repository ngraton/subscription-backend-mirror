from users.models import CustomUser
from subscriptions.models import Subscription
from notifications.models import Notification
from notifications.send_sms import send_sms
import datetime
import sys


now = datetime.datetime.now()

if len(sys.argv) > 1:
  message_text = sys.argv[1]
else:
  message_text = "It's a new month. Log into your account at https://subreckoner.herokuapp.com/ to see what subscriptions are due this month."

users_with_notification_on = CustomUser.objects.exclude(profile__isnull=True)
notifitions_sent = Notification.objects.filter(time_stamp__year=now.year, time_stamp__month=now.month)
users_to_notify = users_with_notification_on.difference(notifitions_sent.users.all())

for user in users_to_notify:
  phone_number = user.profile.phone_number
  send_sms(phone_number, message_text)
  note = Notification(phone_number=phone_number, user=user.id, message=message_text)
  note.save()
