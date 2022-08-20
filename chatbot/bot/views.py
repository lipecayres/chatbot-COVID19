from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt


account_sid = 'AC1581bccfd6ff396ac6aabf8cf08c25f8'
auth_token = '2f4f23101a654484c2c1cbaddc587d98'
client = Client(account_sid, auth_token)

# Create your views here.

@csrf_exempt
def bot (request):
    
    message = request.POST["Body"]
    senderName = request.POST["ProfileName"]
    senderNumber = request.POST["From"]

    if message == "hi":
        client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=f"Hello {senderName}, how are you?",
                              to=senderNumber
                          )
    return HttpResponse("hello")