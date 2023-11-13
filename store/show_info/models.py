from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField('Product name', max_length=255)
    price = models.PositiveIntegerField('Price')
    quantity = models.PositiveIntegerField('Quantity')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Category')
    date = models.DateField('Date add', auto_now_add=True)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.price)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(force_insert, force_update, using, update_fields)


class Category(models.Model):
    name = models.CharField('Category name', max_length=255)

    def __str__(self):
        return self.name
