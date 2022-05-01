# Generated by Django 3.1.13 on 2022-04-06 04:48

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtaildocs', '0012_uploadeddocument'),
        ('misional', '0135_auto_20220405_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConoceUnidadResultadosPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro_title', models.CharField(default='Unidad de Resultados', max_length=254, verbose_name='Título de la sección')),
                ('intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('link_pbi', models.URLField(blank=True, help_text='Link de acceso al tablero Power BI', verbose_name='Link tablero Power BI')),
                ('alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('text_link', wagtail.core.fields.RichTextField(blank=True, help_text='Descripción del elemento, longitud recomendada 85 caracteres', null=True, verbose_name='Descripción')),
                ('button_title', models.CharField(help_text='Título del boton', max_length=254, verbose_name='Título del boton')),
                ('link_mapa', models.URLField(blank=True, verbose_name='Link del mapa')),
                ('featured_link', wagtail.core.fields.StreamField([('Enlace', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local:', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False))]))], blank=True, verbose_name='Enlace destacado')),
                ('document_mapa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document', verbose_name='Documento del mapa')),
                ('image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
                ('image_link', models.ForeignKey(blank=True, help_text='Tamaño recomendado, Alto: 375px, Ancho:1920px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]