# Generated by Django 3.1.13 on 2022-03-25 03:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0052_auto_20220324_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificacionesdisciplinariaspage',
            name='historical_list',
            field=wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento (Opcional)', label='Título', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('documents', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]), blank=True, help_text='Lista', icon='list-ul', label='Lista', required=False))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista'),
        ),
    ]
