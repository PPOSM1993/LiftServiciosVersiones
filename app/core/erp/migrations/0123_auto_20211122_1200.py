# Generated by Django 3.1.7 on 2021-11-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0122_auto_20211108_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='preciocompra',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio Compra'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pvp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio Venta'),
        ),
    ]
