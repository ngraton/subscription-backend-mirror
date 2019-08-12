from users.models import Profile
from subscriptions.models import Subscription
from notifications.models import Notification
from notifications.send_sms import send_sms
import datetime

from django.core.management.base import BaseCommand

class Command(BaseCommand):
  help = "<appropriate help text here>"
  def handle(self, *args, **options):
    now = datetime.datetime.now()
    print(now.day)

    message_text = "It's a new month. Log into your account at https://subreckoner.herokuapp.com/ to see what subscriptions are due this month."

    if now.day == 12:
      profiles = Profile.objects.all()
      # notifitions_sent = CustomUser.objects.filter(notifications__time_stamp__year=now.year, notifications__time_stamp__month=now.month)
      # users_to_notify = users_with_notification_on.difference(notifitions_sent)

      for profile in profiles:
        phone_number = profile.phone_number
        print(phone_number)
        send_sms(phone_number, message_text)
        note = Notification(phone_number=phone_number, user=profile.user, message=message_text)
        note.save()
