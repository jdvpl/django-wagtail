# Generated by Django 3.1.13 on 2021-12-05 02:31

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.contrib.routable_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('common', '0013_auto_20211125_1214'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtaildocs', '0012_uploadeddocument'),
        ('misional', '0084_auto_20211204_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubastasDocumentoUnidadIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='SubastasDocumentoUnidadPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', models.TextField(help_text='Texto que describe el subastasdocumentounidad', verbose_name='Introducción')),
                ('city', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('date_published', models.DateField(null=True, verbose_name='Fecha de publicación')),
                ('document_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document', verbose_name='SubastasDocumentoUnidad')),
                ('image', models.ForeignKey(help_text='Imagen de presentación para el subastasdocumentounidad', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen del subastasdocumentounidad')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SubastasDocumentoUnidadSectorRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='subastasdocumentounidad_sector_relationship', to='misional.subastasdocumentounidadpage')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_subastasdocumentounidad_relationship', to='common.sector')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubastasDocumentoUnidadPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='misional.subastasdocumentounidadpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='misional_subastasdocumentounidadpagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='subastasdocumentounidadpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(help_text='A comma-separated list of tags.', through='misional.SubastasDocumentoUnidadPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='SubastasDocumentoUnidadAutorRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_subastasdocumentounidad_relationship', to='common.autor')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='subastasdocumentounidad_autor_relationship', to='misional.subastasdocumentounidadpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
