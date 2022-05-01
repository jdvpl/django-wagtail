# Generated by Django 3.1.13 on 2021-11-09 00:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0100_auto_20211108_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planesprogramaspage',
            name='plans_list',
            field=wagtail.core.fields.StreamField([('Objetivos', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Planes y Programas', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('subtitle', wagtail.core.blocks.TextBlock(blank=False, help_text='Subtítulo del elemento', label='Subtítulo del elemento', required=True)), ('documents_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('documents', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=True))]), blank=True, help_text='Lista de documentos', icon='list-ul', label='Lista de documentos', required=False))]), blank=True, help_text='Lista de elementos', icon='list-ul', label='Lista de elementos', required=False))]), blank=True, help_text='Lista de elementos', icon='list-ul', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista de objetivos'),
        ),
    ]
