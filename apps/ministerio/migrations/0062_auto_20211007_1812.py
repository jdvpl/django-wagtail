# Generated by Django 3.1.13 on 2021-10-07 23:12

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0061_auto_20211007_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuestogeneralasignadopage',
            name='assigned_taps_list',
            field=wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False)), ('description', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'], help_text='Breve descripción del funcionario.', icon='fa-paragraph', label='Descripción:', required=False, template='blocks/paragraph_block.html'))]), blank=True, help_text='Lista de elementos que se presentaran en formato tabla dentro de una pestaña', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Pestañas'),
        ),
        migrations.AlterField(
            model_name='presupuestogeneralasignadopage',
            name='general_taps_list',
            field=wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False)), ('description', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'], help_text='Breve descripción del funcionario.', icon='fa-paragraph', label='Descripción:', required=False, template='blocks/paragraph_block.html'))]), blank=True, help_text='Lista de elementos que se presentaran en formato tabla dentro de una pestaña', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Pestañas'),
        ),
    ]
