# Generated by Django 3.1.13 on 2021-12-02 02:34

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('misional', '0048_auto_20211201_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReglamentosTecnicosPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('menu_list', wagtail.core.fields.StreamField([('Items', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del elemento', label='Título', required=True)), ('main_description', wagtail.core.blocks.RichTextBlock(help_text='Descripción', label='Descripción', required=True))]))], blank=True, verbose_name='Casos de éxito')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='DatosSectorPage',
        ),
    ]
