from django.shortcuts import render
from django.http import HttpResponse
def myfunction(request):
	import datetime
	a=datetime.datetime.now().date()
	s='<body bgcolor="black"><h1><font color="white"> CURRENT DATE: ' + str(a) + '</h1></body>'
	return HttpResponse(s)

# Create your views here.
