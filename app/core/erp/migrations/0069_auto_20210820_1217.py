# Generated by Django 3.1.7 on 2021-08-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0068_auto_20210820_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formaspago',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Tipo de Pago'),
        ),
    ]
