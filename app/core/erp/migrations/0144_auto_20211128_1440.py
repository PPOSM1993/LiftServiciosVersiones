# Generated by Django 3.1.7 on 2021-11-28 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0143_auto_20211128_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='names',
            new_name='name',
        ),
    ]