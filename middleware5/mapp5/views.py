from django.shortcuts import render
from django.http import HttpResponse
def func(request):
	a=""
	for i in range(1,11):
		a +="5 * {} = {}<br>".format(i,5*i)
	s='<h1>' +str(a)+ ' </h1>'
	return HttpResponse(s)

# Create your views here.
