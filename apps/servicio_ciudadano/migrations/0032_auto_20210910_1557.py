# Generated by Django 3.1.13 on 2021-09-10 20:57

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_ciudadano', '0031_auto_20210910_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plananticorrucionpage',
            name='management_list',
            field=wagtail.core.fields.StreamField([('Foross', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo del elemento', label='Titulo', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Gestión Documental'),
        ),
        migrations.AlterField(
            model_name='plananticorrucionpage',
            name='plans_list',
            field=wagtail.core.fields.StreamField([('Planes', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo del elemento', label='Titulo', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Plan anticorrupción'),
        ),
        migrations.AlterField(
            model_name='plananticorrucionpage',
            name='reports_list',
            field=wagtail.core.fields.StreamField([('Informes', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo del elemento', label='Titulo', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Informes y publicaciones'),
        ),
        migrations.AlterField(
            model_name='rendicioncuentaspage',
            name='plans_list',
            field=wagtail.core.fields.StreamField([('Items', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo del elemento', label='Titulo', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Items'),
        ),
        migrations.AlterField(
            model_name='serviciociudanopage',
            name='services_list',
            field=wagtail.core.fields.StreamField([('Servicios', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo del elemento', label='Titulo', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Servicios'),
        ),
    ]
