# Generated by Django 3.1.7 on 2021-08-26 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0100_auto_20210825_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcat',
            field=models.ForeignKey(default=101, on_delete=django.db.models.deletion.PROTECT, to='erp.subcategory', verbose_name='Proveedor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.proveedor', verbose_name='Subcategoría'),
        ),
    ]
