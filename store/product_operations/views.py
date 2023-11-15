from django.shortcuts import render, redirect
from common import product_valid as pv
from show_info.models import *


def product_create_view(request):
    valid, success = True, False
    category_list = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')

        valid = pv.create_valid(request.POST, len(category_list))

        if valid:
            success = True
            product = Product(name=name, price=price, quantity=quantity, category=Category.objects.get(pk=category))
            product.save()

            return redirect('product_list_page')

    context = {
        'title': 'Create',
        'category_list': category_list,
        'valid': valid,
        'success': success
    }

    return render(request, 'product_operations/product_create.html', context)


def product_delete(request, p_slug):
    product = Product.objects.get(slug=p_slug).delete()

    return redirect('product_list_page')


def product_update(request, p_slug):
    product = Product.objects.get(slug=p_slug)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.category = Category.objects.get(pk=request.POST.get('category'))

        product.save()

        return redirect('product_list_page')

    context = {'product': product,
               'category_list': Category.objects.all()}

    return render(request, 'product_operations/product_update.html', context)
