from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
	a=30
	b=40
	c=a + b
	s='<h1>' +str(a)+ ' plus ' +str(b)+ ' equal ' +str(c)+ '</h1>'
	return HttpResponse(s)
# Create your views here.
