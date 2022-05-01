# Generated by Django 3.1.13 on 2021-11-08 23:21

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0099_auto_20211108_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planesprogramaspage',
            name='plans_list',
            field=wagtail.core.fields.StreamField([('Objetivos', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Planes y Programas', label='Título', required=True)), ('subitems', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('subtitle', wagtail.core.blocks.TextBlock(blank=False, help_text='Subtítulo del elemento', label='Subtítulo del elemento', required=True)), ('documents', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(blank=False, help_text='Título del elemento', label='Título del elemento', required=True)), ('subtitle', wagtail.core.blocks.TextBlock(blank=False, help_text='Subtítulo del elemento', label='Subtítulo del elemento', required=True))]), blank=True, help_text='Lista de elementos', icon='list-ul', label='Lista de elementos', required=False))]), blank=True, help_text='Lista de elementos', icon='list-ul', label='Lista de elementos', required=False))]))], blank=True, verbose_name='Lista de objetivos'),
        ),
    ]
