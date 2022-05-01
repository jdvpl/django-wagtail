# Generated by Django 3.1.10 on 2021-07-23 14:27

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('ministerio', '0037_auto_20210723_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestiondelainformacion',
            name='elementos',
            field=wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Título que describe el elemento de cultura corporativa.', label='Título del Elemento', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen que representa el elemento de cultura corporativa.', label='Imagen', required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla).', label='Texto alternativo', required=False)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ul', 'ol', 'italic', 'link', 'hr'], help_text='Texto descriptivo del elemento de cultura corporativa.', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html'))]))], blank=True, verbose_name='Adicione elementos informativos'),
        ),
        migrations.AddField(
            model_name='gestiondelainformacion',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='gestiondelainformacion',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción'),
        ),
    ]
