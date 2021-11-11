# Generated by Django 3.1.7 on 2021-08-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0085_auto_20210821_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Permiso',
                'verbose_name_plural': 'Permisos',
                'ordering': ['id'],
            },
        ),
    ]
