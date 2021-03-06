# Generated by Django 3.1.7 on 2021-04-23 14:40

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsvg', '0002_svg_edit_code'),
        ('ministerio', '0015_auto_20210423_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='estructurasectorpage',
            name='related_entities',
            field=wagtail.core.fields.StreamField([('Entidad_Vinculada', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Texto que será mostrado al público.', label='Nombre de la entidad', required=True)), ('image_color', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen a color de la entidad', label='Imagen a color', required=True)), ('image_black', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen en blanco y negro', label='Imagen en blanco y negro', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Descripción de la empresa.', label='Descripción de la empresa', required=True))]))], blank=True, verbose_name='Entidades vinculadas'),
        ),
        migrations.AddField(
            model_name='estructurasectorpage',
            name='related_entities_logo',
            field=models.ForeignKey(help_text='Icono del componente en formato SVG', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg', verbose_name='Icono del componente'),
        ),
        migrations.AddField(
            model_name='estructurasectorpage',
            name='related_entities_title',
            field=models.CharField(help_text='Título del componente', max_length=255, null=True, verbose_name='Título del componente'),
        ),
        migrations.AlterField(
            model_name='estructurasectorpage',
            name='sector_entities',
            field=wagtail.core.fields.StreamField([('Entidad_Adscrita', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Texto que será mostrado al público.', label='Nombre de la entidad', required=True)), ('image_color', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen a color de la entidad', label='Imagen a color', required=True)), ('image_black', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen en blanco y negro', label='Imagen en blanco y negro', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Descripción de la empresa.', label='Descripción de la empresa', required=True))]))], blank=True, verbose_name='Entidades adscritas'),
        ),
        migrations.AlterField(
            model_name='estructurasectorpage',
            name='sector_entities_logo',
            field=models.ForeignKey(help_text='Icono del componente en formato SVG', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg', verbose_name='Icono del componente'),
        ),
        migrations.AlterField(
            model_name='estructurasectorpage',
            name='sector_entities_title',
            field=models.CharField(help_text='Título del componente', max_length=255, null=True, verbose_name='Título del componente'),
        ),
    ]
