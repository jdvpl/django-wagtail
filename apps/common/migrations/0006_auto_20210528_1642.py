# Generated by Django 3.1.7 on 2021-05-28 21:42

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20210519_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliatedentitiesblock',
            name='sector_company',
            field=wagtail.core.fields.StreamField([('Entidad_Adscrita', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Texto que serÃ¡ mostrado al pÃºblico.', label='Nombre de la entidad', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen de la entidad', label='Imagen', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una pÃ¡gina local.', label='Link a pÃ¡gina local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una pÃ¡gina externa. Si este campo estÃ¡ completo, no se tendrÃ¡ en cuenta el link a pÃ¡gina local.', label='Link a pÃ¡gina externa', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text=None, label='DescripciÃ³n de la empresa', required=True))]))], blank=True, verbose_name='Entidad Adscrita'),
        ),
        migrations.AlterField(
            model_name='footerblock',
            name='contact_info',
            field=wagtail.core.fields.RichTextField(help_text='InformaciÃ³n de contacto', verbose_name='InformaciÃ³n de contacto'),
        ),
        migrations.AlterField(
            model_name='footerblock',
            name='general_info',
            field=wagtail.core.fields.RichTextField(help_text='InformaciÃ³n de la instituciÃ³n', verbose_name='InformaciÃ³n General'),
        ),
        migrations.AlterField(
            model_name='footerblock',
            name='social_networks',
            field=wagtail.core.fields.StreamField([('Redes_Sociales', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Texto del link que serÃ¡ mostrado al pÃºblico.', label='Texto del link:', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Texto del link que serÃ¡ mostrado al pÃºblico.', label='Imagen:', required=True)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Enlace hacia la pÃ¡gina.', label='Link a pÃ¡gina externa:', required=True))]))], blank=True, verbose_name='Redes Sociales'),
        ),
        migrations.AlterField(
            model_name='headerblock',
            name='links',
            field=wagtail.core.fields.StreamField([('enlaces', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(blank=False, help_text='Texto del link que serÃ¡ mostrado al pÃºblico.', label='Texto del link:', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una pÃ¡gina local.', label='Link a pÃ¡gina local:', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una pÃ¡gina externa. Si este campo estÃ¡ completo, no se tendrÃ¡ en cuenta el link a pÃ¡gina local.', label='Link a pÃ¡gina externa:', required=False))]))], blank=True, verbose_name='Enlaces de gobierno'),
        ),
        migrations.AlterField(
            model_name='relatedentitiesblock',
            name='sector_company',
            field=wagtail.core.fields.StreamField([('Entidad_Vinculada', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Texto que serÃ¡ mostrado al pÃºblico.', label='Nombre de la entidad', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen de la entidad', label='Imagen', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una pÃ¡gina local.', label='Link a pÃ¡gina local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una pÃ¡gina externa. Si este campo estÃ¡ completo, no se tendrÃ¡ en cuenta el link a pÃ¡gina local.', label='Link a pÃ¡gina externa', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text=None, label='DescripciÃ³n de la empresa', required=True))]))], blank=True, verbose_name='Entidad Vinculadas'),
        ),
    ]
