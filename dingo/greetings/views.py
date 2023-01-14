from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greetings(request):
   return HttpResponse("Hello World!")

def helloname(request, name):
   return HttpResponse("Hello " + name.capitalize() + "!")