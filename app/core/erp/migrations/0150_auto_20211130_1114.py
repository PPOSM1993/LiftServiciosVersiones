# Generated by Django 3.1.7 on 2021-11-30 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0149_auto_20211128_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='prove',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.proveedor'),
        ),
    ]
