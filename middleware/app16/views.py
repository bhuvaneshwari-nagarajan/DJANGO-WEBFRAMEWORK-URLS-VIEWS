from django.shortcuts import render
from django.http import HttpResponse
def myfunc(request):
	print("The Middleware")
	return HttpResponse('<h1>Application Running Successfully</h1>')

# Create your views here.
