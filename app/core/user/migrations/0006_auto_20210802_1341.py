# Generated by Django 3.1.7 on 2021-08-02 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_dni'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dni',
            new_name='dniuser',
        ),
    ]
