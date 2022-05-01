# Generated by Django 3.1.7 on 2021-04-14 18:03

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0008_auto_20210413_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culturacorporativapage',
            name='corporate_culture',
            field=wagtail.core.fields.StreamField([('Cultura_Corporativa', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen que representa el elemento de cultura corporativa.', label='Imagen', required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla).', label='Texto alternativo', required=False)), ('name', wagtail.core.blocks.CharBlock(help_text='Título que describe el elemento de cultura corporativa.', label='Título del Elemento', required=True)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ul', 'ol', 'italic', 'link', 'hr'], help_text='Texto descriptivo del elemento de cultura corporativa.', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html'))]))], blank=True, verbose_name='Cultura Corporativa'),
        ),
    ]