# Generated by Django 5.0.4 on 2024-06-01 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar', '0003_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='enlace',
            field=models.URLField(default='null'),
        ),
    ]
