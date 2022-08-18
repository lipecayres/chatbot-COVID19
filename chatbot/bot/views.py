from email import message
from http.client import HTTPResponse
from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

account_sid = 'AC1581bccfd6ff396ac6aabf8cf08c25f8'
auth_token = '40f145233ac72fc86c08f3a0895f07cf'
client = Client(account_sid, auth_token)


# Create your views here.

@csrf_exempt
def bot(request):
    message = request.POST["Body"]
    senderName = request.POST["ProfileName"]
    senderNumber = request.POST["From"]

    if message == "hi":
         client.messages.create(
                              from_='whatsapp:+14155238886',
                              body="Hi {}, how's is it going?".format(sender_name),
                              to=senderNumber
                          )
    return HTTPResponse("hello")