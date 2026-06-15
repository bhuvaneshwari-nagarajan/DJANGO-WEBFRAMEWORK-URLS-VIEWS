from django.shortcuts import render
from django.http import HttpResponse
def myfunction(request):
   import datetime
   a=datetime.datetime.now()
   s='<h1>current date and time' + str(a) +'</h1>'
   return HttpResponse(s)