# Generated by Django 3.1.7 on 2021-08-21 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0082_auto_20210820_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='formapago',
        ),
    ]
