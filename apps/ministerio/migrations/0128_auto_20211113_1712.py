# Generated by Django 3.1.13 on 2021-11-13 22:12

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0127_politicasobjetivoscalidadlpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politicasobjetivoscalidadlpage',
            name='manual_intro_title',
            field=models.CharField(default='Manual de Calidad ', max_length=254, verbose_name='Título de la sección'),
        ),
        migrations.AlterField(
            model_name='politicasobjetivoscalidadlpage',
            name='monitoring_main_intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección uno', null=True, verbose_name='Introducción uno'),
        ),
        migrations.AlterField(
            model_name='politicasobjetivoscalidadlpage',
            name='monitoring_second_intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección dos', null=True, verbose_name='Introducción dos'),
        ),
        migrations.AlterField(
            model_name='politicasobjetivoscalidadlpage',
            name='plan_main_intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección uno', null=True, verbose_name='Introducción uno'),
        ),
        migrations.AlterField(
            model_name='politicasobjetivoscalidadlpage',
            name='plan_second_intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección dos', null=True, verbose_name='Introducción dos'),
        ),
        migrations.AlterField(
            model_name='politicasobjetivoscalidadlpage',
            name='risk_main_intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección uno', null=True, verbose_name='Introducción uno'),
        ),
        migrations.AlterField(
            model_name='politicasobjetivoscalidadlpage',
            name='risk_second_intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección dos', null=True, verbose_name='Introducción dos'),
        ),
    ]
