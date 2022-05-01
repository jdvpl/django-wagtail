# Generated by Django 3.1.13 on 2021-12-25 23:04

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
        ('misional', '0114_auto_20211225_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanesExpansionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro_title', models.CharField(default='Planes de Expansión', max_length=254, verbose_name='Título de la sección')),
                ('intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('link_video', models.URLField(blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', verbose_name='Video')),
                ('alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('intro_one', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('second_links', wagtail.core.fields.StreamField([('Enlaces', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Texto del link que será mostrado al público', label='Título (Opcional)', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del link, solo se acepta imágenes en formato SVG.', label='Icono del elemento (Opcional)', required=False)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento,Si carga un documento la opción de link no se mostrará.', label='Documento', required=False))]))], blank=True, verbose_name='Enlaces secundarios')),
                ('resolutions_title', models.CharField(default='Resoluciones', max_length=254, verbose_name='Título de la sección')),
                ('resolutions_list', wagtail.core.fields.StreamField([('Enlaces', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Texto del link que será mostrado al público', label='Título (Opcional)', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del link, solo se acepta imágenes en formato SVG.', label='Icono del elemento (Opcional)', required=False)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento,Si carga un documento la opción de link no se mostrará.', label='Documento', required=False))]))], blank=True, verbose_name='Enlaces secundarios')),
                ('tab_list_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('intro_tab', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('tab_list', wagtail.core.fields.StreamField([('Tabs', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Pestañas')),
                ('text_link', wagtail.core.fields.RichTextField(blank=True, help_text='Descripción del elemento, longitud recomendada 85 caracteres', null=True, verbose_name='Descripción')),
                ('featured_link', models.URLField(blank=True, verbose_name='Enlace destacado')),
                ('retie_list_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('retie_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('retie_list', wagtail.core.fields.StreamField([('Items', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False)), ('intro', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html'))]))], blank=True, verbose_name='Resoluciones')),
                ('image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
                ('image_link', models.ForeignKey(blank=True, help_text='Tamaño recomendado, Alto: 375px, Ancho:1920px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
