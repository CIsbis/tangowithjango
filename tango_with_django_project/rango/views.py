from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse(
        "<h1>Rango says FRONT ENDS FOR LOSERS</h1>"
        "<a href='/rango/about/'>About</a>"
    )


def about(request):
    return HttpResponse(
        "<h1>Rango says it all about us</h1>"
        "<a href='/rango/'>Index</a>"
    )
