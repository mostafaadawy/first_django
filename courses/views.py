from django.shortcuts import render
from django.views import View
# Create your views here.

# Base VIEW CLASS  = VIEW


class CourseView(View):
    def get(request, *args, **kwargs):
        return render(request, 'about.html', {})

    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})


def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
