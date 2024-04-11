# use API twillio.com - login using google account
import os

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# TODO: Move this values to env var and use from
number_twillio = '$$$$'
number_my = '+$$$$'
account_sid = '$$$$'
auth_token = '$$$$'

#This lines show how use twillio with proxy, and also shou how use env.variables: os.environ['https_proxy']
#How set var from code:
# os.environ['https_proxy'] = 'https://test'
#
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}
# client_for_use_with_proxy = Client(account_sid, auth_token, http_client=proxy_client)

# How find all variables in console use command:
# env or printenv or echo $PATH - to print env var PATH
# How set var from console:
# export TEST_VAR=hello

os.environ.get("TEST_VAR") # access to var from code

client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_=number_twillio,
#   to=number_my,
#   body='Hello from Python application'
# )
#
# print(message.sid)

def send_sms_notification(text):
  message = client.messages.create(
    from_=number_twillio,
    to=number_my,
    body=text
  )

  print(message.sid)