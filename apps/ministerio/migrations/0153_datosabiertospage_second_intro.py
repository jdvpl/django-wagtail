# Generated by Django 3.1.13 on 2021-11-24 17:15

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0152_datosabiertospage'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosabiertospage',
            name='second_intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción'),
        ),
    ]
