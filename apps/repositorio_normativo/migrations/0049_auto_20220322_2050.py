# Generated by Django 3.1.13 on 2022-03-23 01:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0048_notificacionesdisciplinariaspage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendanormativapage',
            name='list_one',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento (Opcional)', label='Título', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True)), ('description', wagtail.core.blocks.TextBlock(blank=False, help_text='Descripción del elemento', label='Descripción del elemento', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(blank=True, help_text='Complete este campo si desea enlazar con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False)), ('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=True))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista'),
        ),
        migrations.AlterField(
            model_name='agendaregulatoriapage',
            name='list_one',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento (Opcional)', label='Título', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True)), ('description', wagtail.core.blocks.TextBlock(blank=False, help_text='Descripción del elemento', label='Descripción del elemento', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(blank=True, help_text='Complete este campo si desea enlazar con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(blank=True, help_text='Complete este campo si desea enlazar con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False)), ('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=True))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista'),
        ),
        migrations.AlterField(
            model_name='notificacionesdisciplinariaspage',
            name='historical_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento (Opcional)', label='Título', required=False)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista'),
        ),
    ]
