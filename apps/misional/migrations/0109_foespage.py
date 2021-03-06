# Generated by Django 3.1.13 on 2021-12-25 16:37

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('misional', '0108_pronepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('retie_list_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('retie_list', wagtail.core.fields.StreamField([('Items', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Seleccione un documento', label='Resolución', required=False)), ('intro', wagtail.core.blocks.RichTextBlock(help_text='Texto descriptivo', icon='fa-paragraph', label='Descripción', required=False, template='blocks/paragraph_block.html'))]))], blank=True, verbose_name='Actas CAPRONE')),
                ('title_list_one', models.CharField(default='Convocatorias PRONE', max_length=254, verbose_name='Título de la sección')),
                ('list_one', wagtail.core.fields.StreamField([('Lista', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento (Opcional)', label='Título', required=False)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]), blank=True, help_text='Lista de elementos', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
