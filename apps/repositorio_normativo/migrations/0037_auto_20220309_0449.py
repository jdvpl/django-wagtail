# Generated by Django 3.1.13 on 2022-03-09 04:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0036_auto_20220309_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edictospage',
            name='edict_list',
            field=wagtail.core.fields.StreamField([('Items', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Acto Administrativo', required=False)), ('intro_1', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='No. Proceso o fecha de publicación', required=False, template='blocks/paragraph_block.html')), ('intro_2', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Nombre del Interesado', required=False, template='blocks/paragraph_block.html')), ('intro_3', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Sección', required=False, template='blocks/paragraph_block.html')), ('intro_4', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Fecha de emisión', required=False, template='blocks/paragraph_block.html'))]))], blank=True, verbose_name='Lista Enlaces '),
        ),
    ]
