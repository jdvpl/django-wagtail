# Generated by Django 3.1.13 on 2021-09-02 23:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_infoentitiesblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliatedentitiesblock',
            name='sector_company',
            field=wagtail.core.fields.StreamField([('Entidad_Adscrita', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Nombre de la entidad que será mostrado al público', label='Nombre de la entidad', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Logotipo de la entidad', label='Logotipo de la entidad', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Descripción de la entidad', label='Descripción de la entidad', required=True))]))], blank=True, verbose_name='Entidad Adscrita'),
        ),
        migrations.AlterField(
            model_name='footerblock',
            name='contact_info',
            field=wagtail.core.fields.RichTextField(help_text='=Información de contacto', verbose_name='Información de contacto'),
        ),
        migrations.AlterField(
            model_name='footerblock',
            name='social_networks',
            field=wagtail.core.fields.StreamField([('Redes_Sociales', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Texto del link que será mostrado al público', label='Texto del link', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Icono', label='Icono de la red social', required=True)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Enlace hacia la página', label='Link hacia la red social', required=True))]))], blank=True, verbose_name='Redes Sociales'),
        ),
        migrations.AlterField(
            model_name='headerblock',
            name='links',
            field=wagtail.core.fields.StreamField([('enlaces', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(blank=False, help_text='Texto del link que será mostrado al público', label='Texto del link', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Enlaces de gobierno'),
        ),
        migrations.AlterField(
            model_name='infoentitiesblock',
            name='inf_entity',
            field=wagtail.core.fields.StreamField([('Sistema_Informacion', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Nombre de la entidad que será mostrado al público', label='Nombre de la entidad', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Logotipo de la entidad', label='Logotipo de la entidad', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Descripción de la entidad', label='Descripción de la entidad', required=True))]))], blank=True, verbose_name='Define los sistemas de informacion'),
        ),
        migrations.AlterField(
            model_name='relatedentitiesblock',
            name='sector_company',
            field=wagtail.core.fields.StreamField([('Entidad_Vinculada', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Nombre de la entidad que será mostrado al público', label='Nombre de la empresa', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Logotipo de la empresa', label='Logotipo de la empresa', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False)), ('represent', wagtail.core.blocks.CharBlock(help_text='Digite el nombre completo del representante legal', label='Nombre del representante legal de la empresa', required=True)), ('mail', wagtail.core.blocks.EmailBlock(help_text='Correo Corporativo', label='Correo Corporativo', required=True))]))], blank=True, verbose_name='Entidad Vinculadas'),
        ),
    ]
