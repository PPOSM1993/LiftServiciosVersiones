# Generated by Django 3.1.7 on 2021-08-26 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0112_auto_20210826_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
