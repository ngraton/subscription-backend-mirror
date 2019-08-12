import os

from twilio.rest import Client

def send_sms(phone_number, message):

  account_sid = os.environ['TWILIO_ACCOUNT_SID']
  auth_token = os.environ['TWILIO_AUTH_TOKEN']
  client = Client(account_sid, auth_token)

  message = client.messages \
                  .create(
                      body=message,
                      from_='+13126839646',
                      to=phone_number,
                  )

# print(message.sid)

# send_sms('+18054510685', 'working')