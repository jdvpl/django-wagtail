# Generated by Django 3.1.13 on 2022-03-15 04:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0040_auto_20220314_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decretosmodificatoriodecretopage',
            name='tab_list',
            field=wagtail.core.fields.StreamField([('Tabs', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('decreto', wagtail.core.blocks.RichTextBlock(help_text='N° Decreto', label='N° Decreto', required=True)), ('date', wagtail.core.blocks.CharBlock(help_text='Fecha de expedicion', label='Fecha de expedicion', required=True)), ('epigrafe', wagtail.core.blocks.CharBlock(help_text='Epígrafe', label='Epígrafe', required=True))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Pestañas'),
        ),
    ]
