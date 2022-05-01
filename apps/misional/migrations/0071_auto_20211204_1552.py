# Generated by Django 3.1.13 on 2021-12-04 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('common', '0013_auto_20211125_1214'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('misional', '0070_auto_20211204_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapacidadAutorRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_capacidad_relationship', to='common.autor')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CapacidadPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', models.TextField(help_text='Texto que describe la capacidad', verbose_name='Introducción')),
                ('body', wagtail.core.fields.StreamField([('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', label='Bloque de párrafo', template='news_blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen', required=True)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(label='Texto de la imagen', required=True)), ('text', wagtail.core.blocks.TextBlock(label='Cita', required=False))], label='Bloque de imagen')), ('image_link_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen', required=True)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(label='Texto de la imagen', required=False)), ('text', wagtail.core.blocks.TextBlock(label='Cita', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False))], label='Bloque de imagen con link')), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(help_text='No incluir comillas de inicio', label='Cita')), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='Ej. Mary Berry', required=False))], label='Bloque de citación')), ('embed_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False))], label='Bloque de link')), ('audio_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('audio', wagtailmedia.blocks.AudioChooserBlock(label='Audio', required=False))], label='Bloque de audio')), ('video_block', wagtail.core.blocks.StructBlock([('video_url', wagtail.core.blocks.URLBlock(help_text='El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', label='Link del video', required=False))], label='Bloque de video'))], verbose_name='Cuerpo de la capacidad')),
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
            name='CapacidadPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='misional.capacidadpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='misional_capacidadpagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CapacidadSectorRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='capacidad_sector_relationship', to='misional.capacidadpage')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_capacidad_relationship', to='common.sector')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='NoticiaUnidadResultadosIndexPage',
            new_name='CapacidadIndexPage',
        ),
        migrations.RemoveField(
            model_name='noticiaunidadresultadospage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='noticiaunidadresultadospage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='noticiaunidadresultadospage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='noticiaunidadresultadospagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='noticiaunidadresultadospagetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='noticiaunidadresultadossectorrelationship',
            name='page',
        ),
        migrations.RemoveField(
            model_name='noticiaunidadresultadossectorrelationship',
            name='sector',
        ),
        migrations.DeleteModel(
            name='NoticiaUnidadResultadosAutorRelationship',
        ),
        migrations.DeleteModel(
            name='NoticiaUnidadResultadosPage',
        ),
        migrations.DeleteModel(
            name='NoticiaUnidadResultadosPageTag',
        ),
        migrations.DeleteModel(
            name='NoticiaUnidadResultadosSectorRelationship',
        ),
        migrations.AddField(
            model_name='capacidadpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(help_text='A comma-separated list of tags.', through='misional.CapacidadPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='capacidadautorrelationship',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='capacidad_autor_relationship', to='misional.capacidadpage'),
        ),
    ]
