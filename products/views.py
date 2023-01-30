from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {'object': obj}
    return render(request, "products/product_detail.html", context)


# def product_create_view(request):
#     my_from = RawProductForm()
#     if request.POST:
#         my_from = RawProductForm(request.POST)
#         if my_from.is_valid():
#             print('my_from.cleaned_data', my_from.cleaned_data)
#             Product.objects.create(**my_from.cleaned_data)
#             my_from = RawProductForm()
#         else:
#             print('my_from.errors', my_from.errors)

#     context = {"form": my_from}
#     return render(request, "products/product_test.html", context)

# def product_create_view(request):
#     # print('GET PRINTING', request.GET)
#     # print('POST PRINTING', request.POST)
#     if request.POST:
#         my_new_title = request.POST.get('title')
#         print('my_new_title', my_new_title)
#     context = {}
#     return render(request, "products/product_test.html", context)


def product_create_view(request):
    my_form = ProductForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = ProductForm()

    context = {'form': my_form}
    return render(request, "products/product_create.html", context)


def render_initial_data(request):
    initial_data = {
        'title': 'this is initial data title',
    }
    obj = Product.objects.get(id=1)
    my_form = ProductForm(request.POST or None,
                          initial=initial_data, instance=obj)
    if my_form.is_valid():
        my_form.save()
        my_form = ProductForm()

    context = {'form': my_form}
    return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, id=my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except:
        raise Http404
    context = {'object': obj}
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.POST:
        # confirming delete
        obj.delete()
        print('debug', obj)
        return redirect('/products/')
        # return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {'object_list': queryset}
    return render(request, "products/product_list.html", context)
