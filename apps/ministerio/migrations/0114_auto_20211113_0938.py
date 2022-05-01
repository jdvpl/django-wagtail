# Generated by Django 3.1.13 on 2021-11-13 14:38

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0113_auto_20211113_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plananualadquisicionespage',
            name='data_list',
            field=wagtail.core.fields.StreamField([('Planes', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del portafolio, políticas y/o protocolos de servicio ', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True))]))], blank=True, verbose_name='Planes'),
        ),
    ]
