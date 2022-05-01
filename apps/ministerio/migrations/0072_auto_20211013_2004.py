# Generated by Django 3.1.13 on 2021-10-14 01:04

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0071_auto_20211013_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procesosprocedimientospage',
            name='items_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True)), ('description', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista'),
        ),
    ]
