# Generated by Django 3.1.7 on 2021-11-28 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0142_auto_20211127_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detbuy',
            name='buy',
        ),
        migrations.RemoveField(
            model_name='detbuy',
            name='prod',
        ),
        migrations.DeleteModel(
            name='Buy',
        ),
        migrations.DeleteModel(
            name='DetBuy',
        ),
    ]