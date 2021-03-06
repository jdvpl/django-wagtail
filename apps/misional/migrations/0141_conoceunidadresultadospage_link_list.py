# Generated by Django 3.1.13 on 2022-04-06 05:29

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0140_auto_20220406_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='conoceunidadresultadospage',
            name='link_list',
            field=wagtail.core.fields.StreamField([('Enlaces', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=False)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Icono del elemento que será mostrado al publico, solo se mostrara la imagen si no se ha seleccionado un icono SVG', label='Imagen', required=False)), ('title_button', wagtail.core.blocks.CharBlock(help_text='Título del boton para descargar', label='Título Boton', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Corta descripción del elemento', label='Descripción', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Complete este campo si el elemento debe presentar un documento como enlace directo', label='Documento', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Enlaces de la sección documentos'),
        ),
    ]
