# Generated by Django 3.1.13 on 2022-03-03 22:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0024_merge_20220303_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticiosoadministrativopage',
            name='notiadmin_list',
            field=wagtail.core.fields.StreamField([('Items', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False)), ('intro_1', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html')), ('intro_2', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html')), ('intro_3', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html')), ('intro_4', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html'))]))], blank=True, verbose_name='Relación Cronológica RETIE '),
        ),
    ]
