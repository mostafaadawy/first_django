from django.shortcuts import render
from django.views import View
# Create your views here.

# Base VIEW CLASS  = VIEW


class CourseView(View):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    # def post(self, request, *args, **kwargs):
    #     return render(request, 'about.html', {})


def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
