# Generated by Django 3.1.7 on 2021-08-25 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0095_auto_20210825_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.category', verbose_name='Subcategoría'),
        ),
    ]
