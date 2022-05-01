# Generated by Django 3.1.13 on 2021-11-21 22:56

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sala_prensa', '0048_auto_20211121_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventopage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', label='Bloque de párrafo', template='news_blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen', required=True)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(label='Texto de la imagen', required=True)), ('text', wagtail.core.blocks.TextBlock(label='Cita', required=False))], label='Bloque de imagen')), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(help_text='No incluir comillas de inicio', label='Cita')), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='Ej. Mary Berry', required=False))], label='Bloque de citación')), ('embed_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen', required=True)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(label='Texto de la imagen', required=True)), ('text', wagtail.core.blocks.TextBlock(label='Cita', required=False))], label='Bloque de link'))], verbose_name='Cuerpo del evento'),
        ),
        migrations.AlterField(
            model_name='noticiapage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', label='Bloque de párrafo', template='news_blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen', required=True)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(label='Texto de la imagen', required=True)), ('text', wagtail.core.blocks.TextBlock(label='Cita', required=False))], label='Bloque de imagen')), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(help_text='No incluir comillas de inicio', label='Cita')), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='Ej. Mary Berry', required=False))], label='Bloque de citación')), ('embed_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen', required=True)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(label='Texto de la imagen', required=True)), ('text', wagtail.core.blocks.TextBlock(label='Cita', required=False))], label='Bloque de link'))], verbose_name='Cuerpo de la noticia'),
        ),
    ]
