# Generated by Django 3.1.13 on 2022-02-24 05:20

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0008_agendanormativapage_menu_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendanormativapage',
            name='list_one',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento (Opcional)', label='Título', required=False)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=True)), ('starred', wagtail.core.blocks.ChoiceBlock(choices=[('true', 'Destacado')], help_text='Seleccione Destacado si el archivo debe resaltarse en la lista de elementos', label='Item destacado', required=False))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista'),
        ),
    ]
