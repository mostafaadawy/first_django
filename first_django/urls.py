"""first_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view, social_view
from products.views import product_detail_view, product_create_view, render_initial_data, dynamic_lookup_view, product_delete_view, product_list_view
urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contacts'),
    path('product_list/', product_list_view, name='list'),
    path('about/', about_view, name='about'),
    path('social/', social_view, name='social'),
    path('products/', product_detail_view, name="product_detail"),
    path('create/', product_create_view, name="product_create"),
    path('initial/', render_initial_data, name="product_render_initials"),
    path('product/<int:my_id>/', dynamic_lookup_view, name="dynamic_lookup_view"),
    path('products/<int:my_id>/delete/',
         product_delete_view, name="product_delete"),
    path('admin/', admin.site.urls),
]
