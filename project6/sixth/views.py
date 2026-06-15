from django.shortcuts import render
from django.http import HttpResponse
def myfunction(request):
	import random
	x=random.random()
	s='<html><body bgcolor="pink"><h1 color="black"> Random Numbers : ' +str(x)+ '</h1></body></html>'
	return HttpResponse(s)
