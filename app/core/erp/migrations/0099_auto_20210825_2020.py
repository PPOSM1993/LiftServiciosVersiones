# Generated by Django 3.1.7 on 2021-08-26 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0098_auto_20210825_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['id'], 'verbose_name': 'Subcategoria', 'verbose_name_plural': 'Subcategorias'},
        ),
    ]
