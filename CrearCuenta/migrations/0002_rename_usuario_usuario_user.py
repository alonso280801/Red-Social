# Generated by Django 5.0.4 on 2024-06-03 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CrearCuenta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario',
            new_name='user',
        ),
    ]
