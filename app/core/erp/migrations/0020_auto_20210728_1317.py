# Generated by Django 3.1.7 on 2021-07-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0019_auto_20210728_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Telefono'),
        ),
    ]