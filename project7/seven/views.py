from django.shortcuts import render
from django.http import HttpResponse
def myfunction(request):
	import random
	colors=["red","blue","green","yellow"]
	c=random.choice(colors)
	s=f'<html><body style="background:{c};"><h1>{c}</h1></body></html>'
	return HttpResponse(s)


# Create your views here.
