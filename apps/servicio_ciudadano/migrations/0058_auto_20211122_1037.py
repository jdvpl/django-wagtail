# Generated by Django 3.1.13 on 2021-11-22 15:37

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_ciudadano', '0057_auto_20211114_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plananticorrucionpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción'),
        ),
    ]