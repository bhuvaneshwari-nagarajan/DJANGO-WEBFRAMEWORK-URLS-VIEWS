from django.shortcuts import render
from django.http import HttpResponse
def func(request):
	import math
	a=2
	x=math.pow(a,5)

	s='<h1>Square value is' +str(x)+'</h1>'
	return HttpResponse(s)

# Create your views here.
