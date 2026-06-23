from django.shortcuts import render
from django.http import HttpResponse
def helo(request):
	a=3
	b=2
	if (a>b):
		result="A is Greater"
	elif (a<b):
		result="B is Greater"
	else:
		result="Both are Equal"
	x='<h1> A is ' +str(a)+ ' , B is ' +str(b)+ ': ' +str(result)+ '</h1>'
	return HttpResponse(x)

# Create your views here.
