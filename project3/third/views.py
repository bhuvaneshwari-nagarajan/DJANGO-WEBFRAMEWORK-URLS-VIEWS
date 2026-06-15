from django.shortcuts import render
from django.http import HttpResponse
def myfunction(request):
   s='<html><body bgcolor="blue"><h1><font color="white">Hello, World!</h1></body></html>'
   return HttpResponse(s)