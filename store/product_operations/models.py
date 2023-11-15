from django.db import models
from show_info.models import *


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='Product')
    user_name = models.CharField('User name', max_length=255)
    comment = models.TextField('Comment')
    created_add = models.DateField('Date', auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.product.name, self.user_name)
