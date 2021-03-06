# Generated by Django 3.1.13 on 2021-12-04 14:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsvg', '0002_svg_edit_code'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('misional', '0063_auto_20211203_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midstreampage',
            name='plan_title',
            field=models.CharField(default='Impuesto de Transporte', max_length=254, verbose_name='Título de la sección'),
        ),
        migrations.AlterField(
            model_name='midstreampage',
            name='price_title',
            field=models.CharField(default='Transporte de Biocombustibles', max_length=254, verbose_name='Título de la sección'),
        ),
        migrations.AlterField(
            model_name='midstreampage',
            name='second_intro_one',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción primer bloque', null=True, verbose_name='Introducción'),
        ),
        migrations.AlterField(
            model_name='midstreampage',
            name='sicom_title',
            field=models.CharField(default='Transporte de crudos', max_length=254, verbose_name='Título de la sección'),
        ),
        migrations.CreateModel(
            name='UpstreamPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('exploration_exploitation_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('exploration_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('exploration_intro_two', wagtail.core.fields.RichTextField(blank=True, help_text='Bloque de texto', null=True, verbose_name='Bloque de texto')),
                ('exploration_list', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.RichTextBlock(help_text='Breve descripción', icon='fa-paragraph', label='Descripción', required=False))]), blank=True, help_text='Lista de elementos que se presentaran', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Acordeón')),
                ('exploration_intro_three', wagtail.core.fields.RichTextField(blank=True, help_text='Bloque de texto', null=True, verbose_name='Bloque de texto')),
                ('exploitation_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('exploitation_intro_two', wagtail.core.fields.RichTextField(blank=True, help_text='Bloque de texto', null=True, verbose_name='Bloque de texto')),
                ('exploitation_list', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.RichTextBlock(help_text='Breve descripción', icon='fa-paragraph', label='Descripción', required=False))]), blank=True, help_text='Lista de elementos que se presentaran', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Acordeón')),
                ('exploitation_intro_three', wagtail.core.fields.RichTextField(blank=True, help_text='Bloque de texto', null=True, verbose_name='Bloque de texto')),
                ('certificates_title', models.CharField(blank=True, help_text='Título', max_length=255, null=True, verbose_name='Título de la sección')),
                ('certificates_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Bloque de texto', null=True, verbose_name='Bloque de texto')),
                ('certificates_list', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.RichTextBlock(help_text='Breve descripción', icon='fa-paragraph', label='Descripción', required=False))]), blank=True, help_text='Lista de elementos que se presentaran', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Acordeón')),
                ('form_title', models.CharField(blank=True, help_text='Título', max_length=255, null=True, verbose_name='Título de la sección')),
                ('form_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Bloque de texto', null=True, verbose_name='Bloque de texto')),
                ('form_list', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Pestañas')),
                ('slider_title', models.CharField(blank=True, help_text='Título', max_length=255, null=True, verbose_name='Título de la sección')),
                ('slider', wagtail.core.fields.StreamField([('slider', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del slider', label='Título', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Tamaño recomendado de la imagen 1820px pixeles.', label='Imagen', required=True)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla).', label='Texto alternativo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(blank=False, help_text='Complete este campo si desea enlazar este slider con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(blank=False, help_text='Complete este campo si desea enlazar este slider con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'], help_text='Texto descriptivo del slider.', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html'))]))], blank=True, verbose_name='Slider')),
                ('myths_title', models.CharField(blank=True, help_text='Título', max_length=255, null=True, verbose_name='Título de la sección')),
                ('tabs_title', models.CharField(blank=True, help_text='Título', max_length=255, null=True, verbose_name='Título de la sección')),
                ('tabs', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=True)), ('intro', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html')), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False)), ('date', wagtail.core.blocks.TextBlock(blank=False, help_text='Fecha en formato 28/02/2021', label='Fecha', required=True)), ('description', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'hr'], help_text='Breve descripción', icon='fa-paragraph', label='Descripción:', required=False, template='blocks/paragraph_block.html'))]), blank=True, help_text='Lista de elementos que se presentaran en formato tabla dentro de una pestaña', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Pestañas')),
                ('exploitation_icon', models.ForeignKey(help_text='Icono', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg', verbose_name='Icono')),
                ('exploration_icon', models.ForeignKey(help_text='Icono', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg', verbose_name='Icono')),
                ('myths_image_one', models.ForeignKey(blank=True, help_text='Imagen', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
                ('myths_image_two', models.ForeignKey(blank=True, help_text='Imagen', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
