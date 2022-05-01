# Generated by Django 3.1.13 on 2022-03-01 21:11

import apps.repositorio_normativo.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0021_remove_agendanormativapage_data_description_acordeon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendanormativapage',
            name='items_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('description_block', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=False)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True)), ('description', wagtail.core.blocks.TextBlock(blank=False, help_text='Descripción del elemento', label='Descripción del elemento', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(blank=True, help_text='Complete este campo si desea enlazar con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False))], closed=False, icon='link', value_class=apps.repositorio_normativo.blocks.LinkStructValue), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista'),
        ),
    ]
