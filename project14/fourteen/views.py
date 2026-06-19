from django.shortcuts import render
from django.http import HttpResponse
def myfunc(request):
	a=int(input("Enter value a:"))
	b=int(input("Enter value b:"))
	if (a>b):
		c="A is Greater"
	else:
		c="B is Greater"
	s='<h1>The value check: ' +str(c)+ '</h1>'
	return HttpResponse(s)

# Create your views here.
