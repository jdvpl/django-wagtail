# Generated by Django 3.1.13 on 2021-11-17 23:59

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_sitemappage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='information_systems',
            field=wagtail.core.fields.StreamField([('Sistema', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del sistema de información', label='Título', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Imagen del sistema de información', label='Imagen', required=True)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla).', label='Texto alternativo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(blank=False, help_text='Complete este campo si desea enlazar este slider con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(blank=False, help_text='Complete este campo si desea enlazar este slider con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False))]))], blank=True, verbose_name='Sistemas de información'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='systems_title',
            field=models.CharField(blank=True, help_text='Título del la sección', max_length=20, null=True, verbose_name='Título del la sección'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slider',
            field=wagtail.core.fields.StreamField([('slider', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del slider', label='Título', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Tamaño recomendado de la imagen 1820px pixeles.', label='Imagen', required=True)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla).', label='Texto alternativo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(blank=False, help_text='Complete este campo si desea enlazar este slider con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(blank=False, help_text='Complete este campo si desea enlazar este slider con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'], help_text='Texto descriptivo del slider.', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html'))]))], blank=True, verbose_name='Slider página de Inicio'),
        ),
    ]
