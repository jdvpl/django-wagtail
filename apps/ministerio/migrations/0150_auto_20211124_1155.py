# Generated by Django 3.1.13 on 2021-11-24 16:55

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('ministerio', '0149_auto_20211124_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='estructuraorganizacionalpage',
            name='alt_text',
            field=models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo'),
        ),
        migrations.AddField(
            model_name='estructuraorganizacionalpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='estructuraorganizacionalpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción'),
        ),
        migrations.AddField(
            model_name='estructuraorganizacionalpage',
            name='intro_title',
            field=models.CharField(default='Estructura Organizacional', max_length=254, verbose_name='Título de la sección'),
        ),
        migrations.AddField(
            model_name='estructuraorganizacionalpage',
            name='link_video',
            field=models.URLField(blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', verbose_name='Video'),
        ),
        migrations.AddField(
            model_name='estructuraorganizacionalpage',
            name='second_links',
            field=wagtail.core.fields.StreamField([('Enlaces', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Texto del link que será mostrado al público', label='Título (Opcional)', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True)), ('icono', wagtailsvg.blocks.SvgChooserBlock(help_text='Icono del link, solo se acepta imágenes en formato SVG.', label='Icono del elemento (Opcional)', required=False)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento,Si carga un documento la opción de link no se mostrará.', label='Documento', required=False))]))], blank=True, verbose_name='Enlaces secundarios'),
        ),
    ]
