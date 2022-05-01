# Generated by Django 3.1.7 on 2021-05-07 02:06

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_info', wagtail.core.fields.RichTextField(help_text='Información de la institución', verbose_name='Información General')),
                ('social_networks', wagtail.core.fields.StreamField([('Redes_Sociales', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Texto del link que será mostrado al público.', label='Texto del link:', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Icono.', label='Imagen:', required=True)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Enlace hacia la página.', label='Link a página externa:', required=True))]))], blank=True, verbose_name='Redes Sociales')),
                ('contact_info', wagtail.core.fields.RichTextField(help_text='Información de contacto', verbose_name='Información de contacto')),
            ],
            options={
                'verbose_name_plural': 'Footer',
            },
        ),
        migrations.CreateModel(
            name='HeaderBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', wagtail.core.fields.StreamField([('enlaces', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(blank=False, help_text='Texto del link que será mostrado al público.', label='Texto del link:', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local:', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False))]))], blank=True, verbose_name='Enlaces de gobierno')),
            ],
            options={
                'verbose_name_plural': 'Header',
            },
        ),
    ]
