# Generated by Django 4.2.7 on 2023-11-13 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product name')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date add')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Slug')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='show_info.category', verbose_name='Category')),
            ],
        ),
    ]