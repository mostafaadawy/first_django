from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)
    print('request', request.user)
    # return HttpResponse("<h1>Home Page</h1>")
    # passing the request, file to be rendered and data
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contacts</h1>")


def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>about</h1>")
