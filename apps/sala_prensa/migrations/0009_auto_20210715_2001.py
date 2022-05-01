# Generated by Django 3.1.7 on 2021-07-16 01:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sala_prensa', '0008_auto_20210715_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticiapage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Seleccione un tamaño de encabezado'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')], required=False))], label='Bloque de título')), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', label='Bloque de párrafo', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen', required=True)), ('caption', wagtail.core.blocks.CharBlock(label='Descripción', required=False)), ('attribution', wagtail.core.blocks.CharBlock(label='Autor', required=False))], label='Bloque de imagen')), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(label='Cita')), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='Ej. Mary Berry', required=False))], label='Bloque de citación')), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-link', label='Bloque de enalce', template='blocks/embed_block.html'))], blank=True, verbose_name='Cuerpo de la noticia'),
        ),
    ]
