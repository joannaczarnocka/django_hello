from django.urls import path
from .views import greetings, helloname

urlpatterns = [
   path('', greetings),
   path('<str:name>', helloname),
]