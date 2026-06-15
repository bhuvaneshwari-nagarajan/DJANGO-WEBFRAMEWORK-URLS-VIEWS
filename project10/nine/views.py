from django.shortcuts import render
from django.http import HttpResponse

def myfunction(request):

    s = """
    <html>
    <head>
        <title>My Page</title>
    </head>

    <body style="background:linear-gradient(to right, #141E30, #243B55);">

        <h1 style="
            color:white;
            text-align:center;
            margin-top:100px;
            font-size:50px;
            font-family:Arial;
        ">
            Welcome to Django
        </h1>

        <p style="
            color:yellow;
            text-align:center;
            font-size:25px;
        ">
            My First Django Styled Page
        </p>

    </body>
    </html>
    """

    return HttpResponse(s)

# Create your views here.
