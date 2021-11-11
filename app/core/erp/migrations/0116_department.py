# Generated by Django 3.1.7 on 2021-10-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0115_auto_20211013_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['id'],
            },
        ),
    ]
