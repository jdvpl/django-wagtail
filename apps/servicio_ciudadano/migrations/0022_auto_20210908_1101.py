# Generated by Django 3.1.13 on 2021-09-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_ciudadano', '0021_auto_20210908_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciociudanopage',
            name='intro',
            field=models.TextField(blank=True, help_text='Introducción de la sección', max_length=254, null=True, verbose_name='Introducción'),
        ),
    ]
