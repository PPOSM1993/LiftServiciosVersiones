# Generated by Django 3.1.7 on 2021-08-26 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0106_product_subcat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cat',
        ),
    ]
