from django.shortcuts import render

# Create your views here.


def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
