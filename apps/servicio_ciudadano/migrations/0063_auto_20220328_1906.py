# Generated by Django 3.1.13 on 2022-03-29 00:06

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_ciudadano', '0062_auto_20220328_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciociudanopage',
            name='briefcase_list',
            field=wagtail.core.fields.StreamField([('Portafolio', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del portafolio, políticas y/o protocolos de servicio ', label='Título', required=True)), ('main_description', wagtail.core.blocks.TextBlock(help_text='Descripción principal del portafolio, políticas y/o protocolos de servicio ', label='Descripción principal ', required=True)), ('second_description', wagtail.core.blocks.TextBlock(help_text='Descripción complementaria del portafolio, políticas y/o protocolos de servicio ', label='Descripción complementaria ', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Tamaño recomendado de la imagen 200px X 200px pixeles', label='Imagen', required=False)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False))]))], blank=True, verbose_name='Portafolio, políticas y protocolos de servicio'),
        ),
    ]
