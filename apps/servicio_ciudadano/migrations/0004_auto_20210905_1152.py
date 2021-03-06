# Generated by Django 3.1.13 on 2021-09-05 16:52

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_ciudadano', '0003_auto_20210905_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciociudanopage',
            name='slider',
            field=wagtail.core.fields.StreamField([('slider', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(blank=True, help_text='Tamaño recomendado de la imagen 1820px X 680px pixeles', label='Imagen', required=True)), ('video', wagtail.core.blocks.URLBlock(blank=False, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', label='Link video', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(blank=False, help_text='Complete este campo si desea enlazar este slider con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(blank=False, help_text='Complete este campo si desea enlazar este slider con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False))]))], blank=True, verbose_name='Slider'),
        ),
    ]
