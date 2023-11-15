from django.shortcuts import render, redirect
from .models import *
from product_operations.models import *


def product_list_page(request):
    focus_cat = request.GET

    if focus_cat:
        products = Product.objects.filter(category=Category.objects.get(name=focus_cat['name']).pk)
    else:
        products = Product.objects.all()

    categorys = Category.objects.all()

    context = {'title': 'Product List',
               'products': products,
               'categorys': categorys}

    return render(request, 'show_info/product_list.html', context)


def product_detail_page(request, p_slug):
    product = Product.objects.get(slug=p_slug)
    return render(request, 'show_info/product_detail.html', {'title': 'Product Detail', 'product': product})


def comment_create_view(request, p_slug):
    product = Product.objects.get(slug=p_slug)

    if request.method == 'POST':
        username = request.POST['username']
        comment = request.POST['comment']

        create_comment = Comment()
        create_comment.product = product
        create_comment.user_name = username
        create_comment.comment = comment
        create_comment.save()

    return redirect('product_detail_page', p_slug)
