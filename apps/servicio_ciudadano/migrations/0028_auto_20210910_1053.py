# Generated by Django 3.1.13 on 2021-09-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_ciudadano', '0027_auto_20210910_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forospage',
            name='introduction',
            field=models.TextField(help_text='Texto que describe foro', verbose_name='Introducción'),
        ),
    ]
