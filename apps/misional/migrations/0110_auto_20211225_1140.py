# Generated by Django 3.1.13 on 2021-12-25 16:40

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0109_foespage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foespage',
            name='retie_list',
            field=wagtail.core.fields.StreamField([('Items', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Resolución', required=False)), ('intro', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html'))]))], blank=True, verbose_name='Circulares e Instructivos'),
        ),
        migrations.AlterField(
            model_name='foespage',
            name='title_list_one',
            field=models.CharField(default='Subsidios de Energía Social - FOES', max_length=254, verbose_name='Título de la sección'),
        ),
        migrations.AlterField(
            model_name='pronepage',
            name='retie_list',
            field=wagtail.core.fields.StreamField([('Items', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Resolución', required=False)), ('intro', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html'))]))], blank=True, verbose_name='Actas PRONE'),
        ),
    ]
