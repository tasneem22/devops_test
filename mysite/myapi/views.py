from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from datetime import datetime
import pytz

now = datetime.now(tz=pytz.timezone('Europe/Moscow')).strftime('%H:%M:%S')

def index(request):
    return HttpResponse("HELLO WORLD! CURRENT TIME IN MOSCOW IS : " + now)
