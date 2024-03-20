from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)
    # return HttpResponse(
    #     "<h1>Rango says FRONT ENDS FOR LOSERS</h1>"
    #     "<a href='/rango/about/'>About</a>"
    #     "<a href='/rango/'>Index</a>"
    #
    # )


def about(request):
    return render(request, 'rango/about.html')
    # return HttpResponse(
    #     "<h1>Rango says it all about us</h1>"
    #     "<a href='/rango/'>Index</a>"
    #
    # )
