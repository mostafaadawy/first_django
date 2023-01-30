from django.shortcuts import render
from products.models import Product
from .forms import ProductForm
# Create your views here.


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {'object': obj}
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    context = {}
    return render(request, "products/product_test.html", context)

# def product_create_view(request):
#     # print('GET PRINTING', request.GET)
#     # print('POST PRINTING', request.POST)
#     if request.POST:
#         my_new_title = request.POST.get('title')
#         print('my_new_title', my_new_title)
#     context = {}
#     return render(request, "products/product_test.html", context)


# def product_create_view(request):
#     my_form = ProductForm(request.POST or None)
#     if my_form.is_valid():
#         my_form.save()
#         my_form = ProductForm()

#     context = {'form': my_form}
#     return render(request, "products/product_create.html", context)
