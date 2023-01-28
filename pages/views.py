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
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "My_text": "Context Text",
        "My_number": 123456789,
        "My_List": [111, "111", True]
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})
