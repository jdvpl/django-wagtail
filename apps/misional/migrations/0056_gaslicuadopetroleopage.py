# Generated by Django 3.1.13 on 2021-12-02 16:03

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('misional', '0055_gasnaturalpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='GasLicuadoPetroleoPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('history_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('history', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('chain_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('chain', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('chain_links', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Texto del link que será mostrado al público', label='Título (Opcional)', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del link, solo se acepta imágenes en formato SVG.', label='Icono del elemento (Opcional)', required=False)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento,Si carga un documento la opción de link no se mostrará.', label='Documento', required=False))]))], blank=True, verbose_name='Cadena de valor')),
                ('assigned_tabs_list_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('assigned_tabs_list', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.RichTextBlock(help_text='Breve descripción', icon='fa-paragraph', label='Descripción', required=False))]), blank=True, help_text='Lista de elementos que se presentaran', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Declaración de Producción de Gas Licuado de Petróleo')),
                ('assigned_tabs_list_two', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento que será mostrado al publico', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.RichTextBlock(help_text='Breve descripción', icon='fa-paragraph', label='Descripción', required=False))]), blank=True, help_text='Lista de elementos que se presentaran', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Reglamentación Técnica')),
                ('general_tabs_list', wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Pestañas')),
                ('gas_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('gas', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
