# Generated by Django 3.1.13 on 2022-02-10 03:28

import apps.common.blocks
from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0115_planesexpansionpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='energiareglamentostecnicospage',
            name='elements_list',
            field=wagtail.core.fields.StreamField([('Estudios', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=False)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Icono del elemento que será mostrado al publico, solo se mostrara la imagen si no se ha seleccionado un icono SVG', label='Imagen', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Corta descripción del elemento', label='Descripción', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Complete este campo si el elemento debe presentar un documento como enlace directo', label='Documento', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(blank=False, help_text='Subitems que serán presentados como un listado en la ventana modal ', label='Subitem', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(blank=True, help_text='Complete este campo si desea enlazar con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Complete este campo si el elemento debe presentar un documento como enlace directo', label='Documento', required=False))], closed=False, icon='link', value_class=apps.common.blocks.LinkStructValue), blank=True, help_text='Lista de elementos que se presentaran en la ventana modal, si se agregan ítems en esta sección, no se presentara información de documento o enlace a otra página', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Estudios, investigaciones y otras publicaciones'),
        ),
        migrations.AddField(
            model_name='energiareglamentostecnicospage',
            name='elements_list_title',
            field=models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección'),
        ),
    ]
