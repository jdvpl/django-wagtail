# Generated by Django 3.1.13 on 2021-11-07 00:27

import apps.common.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('ministerio', '0095_auto_20211024_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProyectosInversionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro_title', models.CharField(default='Proyectos de Inversión', max_length=254, verbose_name='Título de la sección')),
                ('intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('assignment_title', models.CharField(default='Informes de Asignación Presupuestal', max_length=254, verbose_name='Título de la sección')),
                ('assignment_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('assignment_list', wagtail.core.fields.StreamField([('Documento', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False))]))], blank=True, verbose_name='Documentos')),
                ('follow_title', models.CharField(default='Informes de Seguimiento - Proyectos de Inversión', max_length=254, verbose_name='Título de la sección')),
                ('follow_list', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False)), ('description', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'], help_text='Breve descripción', icon='fa-paragraph', label='Descripción:', required=False, template='blocks/paragraph_block.html'))]), blank=True, help_text='Lista de elementos que se presentaran en formato tabla dentro de una pestaña', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Acordeón')),
                ('execution_title', models.CharField(default='Ejecución Presupuestal de Inversión Sector Minas y Energía', max_length=254, verbose_name='Título de la sección')),
                ('execution_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('execution_list', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del elemento que será mostrado al publico, solo imágenes en formato SVG.', label='Icono', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(blank=False, help_text='Título del documento', label='Título ', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False))], closed=False, icon='link', value_class=apps.common.blocks.LinkStructValue), blank=True, help_text='Documentos que serán presentados en formato de lista', label='Lista de documentos', required=False))]))], blank=True, verbose_name='Elementos')),
                ('image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
