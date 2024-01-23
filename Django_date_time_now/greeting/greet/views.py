from django.shortcuts import render
from .models import GreetingLog

# Create your views here.
from django.shortcuts import render
from datetime import datetime

def get_greeting():
    current_time = datetime.now().time()

    if current_time.hour < 12:
        greeting = 'Good morning.'
    elif 12 <= current_time.hour < 18:
        greeting = 'Good afternoon.'
    else:
        greeting = 'Good evening.'

    return greeting

def greeting_view(request):
    greeting_message = get_greeting()

    # Log the greeting message
    GreetingLog.objects.create(greeting=greeting_message)

    return render(request, 'greet/greeting.html', {'greeting': greeting_message})
