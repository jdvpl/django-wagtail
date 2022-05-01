# Generated by Django 3.1.13 on 2021-11-06 22:38

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_ciudadano', '0045_auto_20211106_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablaretenciondocumentalpage',
            name='table',
            field=wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('section_code', wagtail.core.blocks.CharBlock(help_text='Código Sección', label='Código Sección', required=False)), ('section', wagtail.core.blocks.TextBlock(help_text='Sección', label='Sección ', required=False)), ('sub_section_code', wagtail.core.blocks.CharBlock(help_text='Código Subsección', label='Código Subsección', required=False)), ('subsection_description', wagtail.core.blocks.TextBlock(help_text='Subsección', label='Subsección', required=False)), ('subsection_document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento para la subsección', label='Documento subsección', required=False)), ('starred', wagtail.core.blocks.ChoiceBlock(choices=[('true', 'Destacado')], help_text='Seleccione Destacado si el archivo debe resaltarse en la lista de elementos', label='Item destacado', required=False))]))], blank=True, verbose_name='Codificación Estructura Organizacional'),
        ),
    ]
