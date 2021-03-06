# Generated by Django 3.1.13 on 2021-10-14 00:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0070_procesosprocedimientospage_items_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procesosprocedimientospage',
            name='items_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True)), ('title', wagtail.core.blocks.CharBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('description', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista'),
        ),
        migrations.AlterField(
            model_name='procesosprocedimientospage',
            name='systems',
            field=wagtail.core.fields.StreamField([('sistemas', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Nombre del sistema al que se enlazará', label='Nombre del sistema', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen del sistema', label='Imagen del sistema', required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del sistema', label='Descripción del sistema', required=True)), ('button_title', wagtail.core.blocks.CharBlock(help_text='Título del boton', label='Título del boton', required=True)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Link a página externa', label='Link a página externa', required=False))]))], blank=True, verbose_name='Sistemas'),
        ),
    ]
