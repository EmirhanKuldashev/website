from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello! Its my project")

def current_date_view(request):
    from datetime import datetime
    return HttpResponse(f"Current date: {datetime.today().strftime('%Y-%m-%d')}")

def goodbye_view(request):
    return HttpResponse("Goodbye user!")

