# Generated by Django 3.1.13 on 2021-09-30 01:56

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0004_auto_20210929_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='misionalpage',
            name='second_links',
            field=wagtail.core.fields.StreamField([('Enlaces', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(help_text='Texto del link que será mostrado al público', label='Texto del link', max_length=20, required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del link, solo se acepta imágenes en formato SVG.', label='Icono del elemento', required=False)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local:', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False))]))], blank=True, verbose_name='Enlaces secundarios'),
        ),
    ]
