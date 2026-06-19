from django.shortcuts import render
from django.http import HttpResponse
def add(request):
	a=30
	b=15
	result= a + b
	s='<h1>value is ' +str(a)+ 'b value' +str(b)+ 'sum value' +str(result) + '</h1>'
	return HttpResponse(s)

# Create your views here.
