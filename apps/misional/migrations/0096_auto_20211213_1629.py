# Generated by Django 3.1.13 on 2021-12-13 21:29

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
        ('wagtaildocs', '0012_uploadeddocument'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailsvg', '0002_svg_edit_code'),
        ('misional', '0095_auto_20211209_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProyectosHidrocarburosPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.TextField(blank=True, help_text='Introducción', null=True, verbose_name='Introducción')),
                ('link_video', models.URLField(blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', verbose_name='Video')),
                ('alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo de la imagen')),
                ('manager', models.CharField(blank=True, max_length=255, verbose_name='Administrador')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Fecha de inicio')),
                ('department', models.TextField(blank=True, help_text='Departamento', verbose_name='Departamento')),
                ('municipality', models.TextField(blank=True, help_text='Municipio', verbose_name='Municipio')),
                ('users', models.TextField(blank=True, help_text='Usuarios', verbose_name='Usuarios')),
                ('latitude', models.FloatField(blank=True, default=0, help_text='Latitud, valores entre -90 y 90', verbose_name='Latitud')),
                ('longitude', models.FloatField(blank=True, default=0, help_text='Longitud, valores entre -180 y 180', verbose_name='Longitud')),
                ('energy_type', models.TextField(blank=True, help_text='Tipo de energía', verbose_name='Tipo de energía')),
                ('document_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document', verbose_name='Anexos')),
                ('icon', models.ForeignKey(help_text='Icono del tipo de energía', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg', verbose_name='Icono del tipo de energía')),
                ('image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProyectosHidrocarburosSectorRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectoshidrocarburos_sector_relationship', to='misional.proyectoshidrocarburospage')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_proyectoshidrocarburos_relationship', to='common.sector')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProyectosHidrocarburosPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='misional.proyectoshidrocarburospage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='misional_proyectoshidrocarburospagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='proyectoshidrocarburospage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(help_text='A comma-separated list of tags.', through='misional.ProyectosHidrocarburosPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='ProyectosHidrocarburosIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.TextField(blank=True, help_text='Introducción', null=True, verbose_name='Introducción')),
                ('link_video', models.URLField(blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', verbose_name='Video')),
                ('alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo de la imagen')),
                ('projects', models.TextField(blank=True, help_text='Proyectos', verbose_name='Proyectos')),
                ('users', models.TextField(blank=True, help_text='Usuarios', verbose_name='Usuarios')),
                ('image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='ProyectosHidrocarburosAutorRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_proyectoshidrocarburos_relationship', to='common.autor')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectoshidrocarburos_autor_relationship', to='misional.proyectoshidrocarburospage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
