# Generated by Django 3.1.13 on 2022-03-16 20:53

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0121_oficinaasuntosambientalessosteniblespage_first_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oficinaasuntosambientalessosteniblespage',
            name='first_image',
        ),
        migrations.AlterField(
            model_name='oficinaasuntosambientalessosteniblespage',
            name='third_text',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Texto de de la sección', null=True, verbose_name='Funciones'),
        ),
    ]
