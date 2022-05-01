# Generated by Django 3.1.7 on 2021-05-07 00:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0017_auto_20210506_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlinternopage',
            name='element',
            field=wagtail.core.fields.StreamField([('Elemento', wagtail.core.blocks.StructBlock([('image_color', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen a color de la entidad', label='Imagen a color', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono de la parte superior izquierda del elemento, solo se acepta imágenes en formato SVG.', label='Icono del elemento', required=True)), ('name', wagtail.core.blocks.CharBlock(help_text='Titulo del elemento.', label='Titulo del elemento', required=True)), ('description', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'], help_text='Texto descriptivo.', icon='fa-paragraph', label='Descripción', required=True)), ('background_color', wagtail.core.blocks.CharBlock(help_text='Color de fondo para el elemento en formato hexadecimal. Ejemplo: #5A0C6D', label='Color de fondo', max_length=7, required=True)), ('text_color', wagtail.core.blocks.CharBlock(help_text='Color de texto en formato hexadecimal. Ejemplo: #5A0C6D', label='Color de texto', max_length=7, required=True))]))], blank=True, verbose_name='Elementos'),
        ),
    ]
