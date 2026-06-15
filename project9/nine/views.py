from django.shortcuts import render
from django.http import HttpResponse
def myfunc(request):
	import random
	x=random.randint(0,100)
	y="Eligible to Voting" if x >= 18 else "Not Eligible"
	s=f'<body bgcolor="black"><h1 style="text-align:center; color:white;"> {y} is {x}</h1></body>'
	return HttpResponse(s) 

# Create your views here.
