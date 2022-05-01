# Generated by Django 3.1.13 on 2021-09-07 22:59

import apps.common.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_ciudadano', '0016_auto_20210907_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciociudanopage',
            name='channel_list',
            field=wagtail.core.fields.StreamField([('Canales', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Titulo', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True)), ('description', wagtail.core.blocks.TextBlock(help_text='Corta descripción del elemento', label='Descripción', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Complete este campo si el elemento debe presentar un documento como enlace directo', label='Documento', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(blank=False, help_text='Subitems que serán presentados como un listado en la ventana modal ', label='Subitem', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(blank=True, help_text='Complete este campo si desea enlazar con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False))], closed=False, icon='link', value_class=apps.common.blocks.LinkStructValue), blank=True, help_text='Lista de elementos que se presentaran en la ventana modal, si se agregan ítems en esta sección, no se presentara información de documento o enlace a otra página', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Canales de atención'),
        ),
    ]
