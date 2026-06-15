from django.shortcuts import render
from django.http import HttpResponse
def myfunction(request):
	import random
	xy=random.randint(0,100)
	a="Even" if xy % 2 == 0 else "Odd" 
	c=f'<h1 bgcolor="black"> {xy} is {a} </h1>'
	return HttpResponse(c)


# Create your views here.
