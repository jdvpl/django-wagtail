# Generated by Django 3.1.13 on 2021-09-29 21:53

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0055_gestiondelainformacion_elements_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestiondelainformacion',
            name='elements',
            field=wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Título que describe el elemento', label='Título del Elemento', required=True)), ('svg_image', wagtailsvg.blocks.SvgChooserBlock(help_text='Imagen', label='Imagen', required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ul', 'ol', 'italic', 'link', 'hr'], help_text='Texto descriptivo del elemento', icon='fa-paragraph', label='=Descripción', required=False, template='blocks/paragraph_block.html')), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False))]))], blank=True, verbose_name='Sistemas de información'),
        ),
    ]
