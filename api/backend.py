from http.server import BaseHTTPRequestHandler
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_phone_number = os.environ['FROM_PHONE_NUMBER'] 
to_phone_number = os.environ['TO_PHONE_NUMBER'] 

client = Client(account_sid, auth_token)

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = client.messages.create(
                              body='Hi there',
                              from_=from_phone_number,
                              to=to_phone_number
                          )
    self.wfile.write(message.sid.encode())
    return
