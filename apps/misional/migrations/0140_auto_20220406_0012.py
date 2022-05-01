# Generated by Django 3.1.13 on 2022-04-06 05:12

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0139_auto_20220406_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='conoceunidadresultadospage',
            name='intro_modelo',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción'),
        ),
        migrations.AddField(
            model_name='conoceunidadresultadospage',
            name='modelo_title',
            field=models.CharField(default='Modelo de Gestión del Cumplimiento', max_length=254, verbose_name='Título de la sección'),
        ),
    ]
