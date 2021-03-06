# Generated by Django 3.1.13 on 2021-11-13 21:25

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('ministerio', '0126_comitesectorialpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticasObjetivosCalidadlPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('politics_title', models.CharField(default='Política de Calidad', max_length=254, verbose_name='Subtítulo de la sección')),
                ('politics_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('quality_objectives_title', models.CharField(default='Política de Calidad', max_length=254, verbose_name='Subtítulo de la sección')),
                ('quality_objectives', wagtail.core.fields.StreamField([('Objetivos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Objetivos de calidad')),
                ('process_intro_title', models.CharField(default='Procesos y Procedimientos', max_length=254, verbose_name='Título de la sección')),
                ('process_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('process_alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('manual_intro_title', models.CharField(default='Procesos y Procedimientos', max_length=254, verbose_name='Título de la sección')),
                ('manual_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('manual_alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('risk_intro_title', models.CharField(default='Riesgos', max_length=254, verbose_name='Título de la sección')),
                ('risk_list', wagtail.core.fields.StreamField([('Documentos', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Texto del link que será mostrado al público', label='Título', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=False)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del link, solo se acepta imágenes en formato SVG.', label='Icono del elemento', required=False)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Documento', required=False))]))], blank=True, verbose_name='Documentos')),
                ('risk_main_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('risk_second_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('risk_alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('monitoring_list', wagtail.core.fields.StreamField([('Seguimiento', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento (Opcional)', label='Título', required=False)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Seguimiento Mapa de Riesgos')),
                ('monitoring_title', models.CharField(default='Seguimiento Mapa de Riesgos', max_length=254, verbose_name='Título de la sección')),
                ('monitoring_main_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección uno', null=True, verbose_name='Introducción')),
                ('monitoring_second_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección dos', null=True, verbose_name='Introducción')),
                ('plan_title', models.CharField(default='Plan de Mejoramiento por Procesos', max_length=254, verbose_name='Título de la sección')),
                ('plan_main_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección uno', null=True, verbose_name='Introducción')),
                ('plan_second_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección dos', null=True, verbose_name='Introducción')),
                ('plan_alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('plan_link', models.URLField(blank=True, help_text='Enlace aplicativo', verbose_name='Enlace')),
                ('plan_list', wagtail.core.fields.StreamField([('Planes', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento (Opcional)', label='Título', required=False)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Plan de Mejoramiento por Procesos')),
                ('plan_video', models.URLField(blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', verbose_name='Video')),
                ('audit_list', wagtail.core.fields.StreamField([('Auditoria', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento (Opcional)', label='Título', required=False)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Auditoías')),
                ('manual_image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
                ('plan_image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
                ('process_image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
                ('risk_image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
