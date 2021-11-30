# Generated by Django 3.1.7 on 2021-11-08 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0117_cargos'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargos',
            name='department',
            field=models.ForeignKey(default=117, on_delete=django.db.models.deletion.PROTECT, to='erp.department', verbose_name='Departamento'),
            preserve_default=False,
        ),
    ]