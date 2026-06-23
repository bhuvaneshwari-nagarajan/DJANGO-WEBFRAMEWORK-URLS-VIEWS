from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
	print(100/0)
	return HttpResponse('<h1>welcome to galwin')