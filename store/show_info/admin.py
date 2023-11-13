from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'date')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
