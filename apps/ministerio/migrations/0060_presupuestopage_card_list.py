# Generated by Django 3.1.13 on 2021-10-07 20:48

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0059_auto_20211007_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuestopage',
            name='card_list',
            field=wagtail.core.fields.StreamField([('Tarjetas', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Texto del link que será mostrado al público', label='Titulo', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del link, solo se acepta imágenes en formato SVG.', label='Icono del elemento', required=False)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local:', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False))]))], blank=True, verbose_name='Lista de tarjetas'),
        ),
    ]
