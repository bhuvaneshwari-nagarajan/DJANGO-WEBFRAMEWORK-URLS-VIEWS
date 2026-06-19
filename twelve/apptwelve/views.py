from django.shortcuts import render
from django.http import HttpResponse
def myfact(request):
	a=5
	fact=1
	for i in range(1,a+1):
		fact=fact*i
	s='<h1>' +str(fact)+ 'is factorial number of 5 </h1>'
	return HttpResponse(s)

# Create your views here.
#n*fact(n-1)