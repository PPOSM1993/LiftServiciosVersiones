# Generated by Django 3.1.7 on 2021-08-15 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0061_auto_20210814_2303'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand',
            new_name='Marca',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='names',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='marca',
        ),
    ]