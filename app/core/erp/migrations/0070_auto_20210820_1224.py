# Generated by Django 3.1.7 on 2021-08-20 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0069_auto_20210820_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detsale',
            name='formapago',
        ),
        migrations.DeleteModel(
            name='FormasPago',
        ),
    ]
