# Generated by Django 3.1.7 on 2021-08-20 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0067_detsale_formapago'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formaspago',
            old_name='formaPago',
            new_name='name',
        ),
    ]
