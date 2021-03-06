# Generated by Django 3.1.13 on 2021-12-05 01:59

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.contrib.routable_page.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtailmedia.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('common', '0013_auto_20211125_1214'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('misional', '0081_auto_20211204_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReglamentacionIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='ReglamentacionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', models.TextField(help_text='Texto que describe la reglamentacion', verbose_name='Introducción')),
                ('body', wagtail.core.fields.StreamField([('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', label='Bloque de párrafo', template='news_blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen', required=True)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(label='Texto de la imagen', required=True)), ('text', wagtail.core.blocks.TextBlock(label='Cita', required=False))], label='Bloque de imagen')), ('image_link_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen', required=True)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(label='Texto de la imagen', required=False)), ('text', wagtail.core.blocks.TextBlock(label='Cita', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False))], label='Bloque de imagen con link')), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(help_text='No incluir comillas de inicio', label='Cita')), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='Ej. Mary Berry', required=False))], label='Bloque de citación')), ('embed_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False))], label='Bloque de link')), ('audio_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('audio', wagtailmedia.blocks.AudioChooserBlock(label='Audio', required=False))], label='Bloque de audio')), ('video_block', wagtail.core.blocks.StructBlock([('video_url', wagtail.core.blocks.URLBlock(help_text='El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', label='Link del video', required=False))], label='Bloque de video'))], verbose_name='Cuerpo de la reglamentacion')),
                ('city', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('date_published', models.DateField(null=True, verbose_name='Fecha de publicación')),
                ('image', models.ForeignKey(help_text='Solo modo horizontal; ancho horizontal entre 1000px y 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen principal')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ReglamentacionSectorRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='reglamentacion_sector_relationship', to='misional.reglamentacionpage')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_reglamentacion_relationship', to='common.sector')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReglamentacionPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='misional.reglamentacionpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='misional_reglamentacionpagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='reglamentacionpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(help_text='A comma-separated list of tags.', through='misional.ReglamentacionPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='ReglamentacionLeyPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro_title', models.CharField(default='Marco normativo del aprovechamiento geotérmico', max_length=254, verbose_name='Título de la sección')),
                ('intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('link_pbi', models.URLField(blank=True, help_text='Link de acceso al tablero Power BI', verbose_name='Link tablero Power BI')),
                ('alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('intro_two', wagtail.core.fields.RichTextField(blank=True, help_text='Bloque de texto', null=True, verbose_name='Bloque de texto')),
                ('news_list_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('news_button_title', models.CharField(blank=True, help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres', max_length=20, null=True, verbose_name='Título botón más información')),
                ('second_links', wagtail.core.fields.StreamField([('Enlaces', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Texto del link que será mostrado al público', label='Título (Opcional)', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del link, solo se acepta imágenes en formato SVG.', label='Icono del elemento (Opcional)', required=False)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento,Si carga un documento la opción de link no se mostrará.', label='Documento', required=False))]))], blank=True, verbose_name='Enlaces secundarios')),
                ('image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
                ('news_list', models.ForeignKey(blank=True, help_text='Seleccione la página del índice de noticias', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Índice de noticias')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ReglamentacionAutorRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_reglamentacion_relationship', to='common.autor')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='reglamentacion_autor_relationship', to='misional.reglamentacionpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
