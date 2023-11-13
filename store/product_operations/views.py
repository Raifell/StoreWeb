from django.shortcuts import render
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

    context = {
        'title': 'Create',
        'category_list': category_list,
        'valid': valid,
        'success': success
    }

    return render(request, 'product_operations/product_create.html', context)
