# Generated by Django 3.1.13 on 2021-09-08 16:03

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_ciudadano', '0023_auto_20210908_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plananticorrucionpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', max_length=254, null=True, verbose_name='Introducción'),
        ),
    ]
