# Generated by Django 3.1.13 on 2021-10-06 01:52

import apps.common.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('transparencia', '0014_auto_20211004_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declaracionrentapage',
            name='documents_list',
            field=wagtail.core.fields.StreamField([('Documentos', wagtail.core.blocks.StreamBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Titulo', required=True)), ('document_block', wagtail.core.blocks.StructBlock([('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(blank=False, help_text='Título del documento', label='Título ', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False))], closed=False, icon='link', value_class=apps.common.blocks.LinkStructValue), blank=True, help_text='Documentos que serán presentados en formato de lista', label='Lista de documentos', required=False))], label='Bloque de imagen'))]))], blank=True, verbose_name='Documentos de la sección'),
        ),
    ]