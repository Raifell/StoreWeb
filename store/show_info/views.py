from django.shortcuts import render
from .models import *


def product_list_page(request):
    products = Product.objects.all()
    return render(request, 'show_info/product_list.html', {'title': 'Product List', 'products': products})


def product_detail_page(request, p_slug):
    product = Product.objects.get(slug=p_slug)
    return render(request, 'show_info/product_detail.html', {'title': 'Product Detail', 'product': product})
