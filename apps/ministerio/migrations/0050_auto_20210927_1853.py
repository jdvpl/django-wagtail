# Generated by Django 3.1.13 on 2021-09-27 23:53

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0049_procesosprocedimientospage_alt_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procesosprocedimientospage',
            name='systems',
            field=wagtail.core.fields.StreamField([('Procesos_y_Procedimientos', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Nombre del sistema al que se enlazará', label='Nombre del sistema', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Imagen del sistema', label='Imagen del sistema', required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del sistema', label='Descripción del sistema', required=True)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Link a página externa', label='Link a página externa', required=False))]))], blank=True, verbose_name='Procesos y Procedimientos'),
        ),
    ]
