# Generated by Django 3.1.7 on 2021-11-28 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0146_auto_20211128_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='name',
            new_name='nombre',
        ),
    ]
