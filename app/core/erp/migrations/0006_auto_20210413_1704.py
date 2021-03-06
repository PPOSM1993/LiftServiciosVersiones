# Generated by Django 3.1.7 on 2021-04-13 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_auto_20210412_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detsale',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.product'),
        ),
        migrations.AlterField(
            model_name='detsale',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.sale'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='cli',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.client'),
        ),
    ]
