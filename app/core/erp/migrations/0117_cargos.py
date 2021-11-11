# Generated by Django 3.1.7 on 2021-11-08 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0116_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'ordering': ['id'],
            },
        ),
    ]
