# Generated by Django 3.1.13 on 2021-11-14 18:13

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0135_auto_20211113_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratacionpage',
            name='menu_list',
            field=wagtail.core.fields.StreamField([('Menu', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]))], blank=True, verbose_name='Items'),
        ),
        migrations.AlterField(
            model_name='plananualvacantespage',
            name='data_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]))], blank=True, verbose_name='Lista'),
        ),
        migrations.AlterField(
            model_name='planestrategicotalentohumanopage',
            name='data_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]))], blank=True, verbose_name='Lista'),
        ),
        migrations.AlterField(
            model_name='planestrategicotecnologiainformacioncomunicacionespage',
            name='data_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]))], blank=True, verbose_name='Lista'),
        ),
        migrations.AlterField(
            model_name='planinstitucionalarchivosentidadpinarpage',
            name='data_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]))], blank=True, verbose_name='Lista'),
        ),
        migrations.AlterField(
            model_name='planprevisionrecursohumanospage',
            name='data_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]))], blank=True, verbose_name='Lista'),
        ),
        migrations.AlterField(
            model_name='planseguridadprivacidadinformacionpage',
            name='data_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]))], blank=True, verbose_name='Lista'),
        ),
        migrations.AlterField(
            model_name='plantratamientoriesgosseguridadprivacidadinformacionpage',
            name='data_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]))], blank=True, verbose_name='Lista'),
        ),
        migrations.AlterField(
            model_name='politicasobjetivoscalidadpage',
            name='audit_list',
            field=wagtail.core.fields.StreamField([('Auditoria', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]))], blank=True, verbose_name='Auditoías'),
        ),
    ]
