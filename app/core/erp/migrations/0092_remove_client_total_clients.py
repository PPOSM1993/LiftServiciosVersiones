# Generated by Django 3.1.7 on 2021-08-24 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0091_client_total_clients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='total_clients',
        ),
    ]
