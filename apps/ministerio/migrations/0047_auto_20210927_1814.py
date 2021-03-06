# Generated by Django 3.1.13 on 2021-09-27 23:14

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('ministerio', '0046_culturacorporativapage_section_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='procesosprocedimientospage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción'),
        ),
        migrations.AddField(
            model_name='procesosprocedimientospage',
            name='intro_title',
            field=models.CharField(default='Procesos', max_length=254, verbose_name='Título de la sección'),
        ),
        migrations.AlterField(
            model_name='procesosprocedimientospage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen'),
        ),
    ]
