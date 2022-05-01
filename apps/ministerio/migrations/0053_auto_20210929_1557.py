# Generated by Django 3.1.13 on 2021-09-29 20:57

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('ministerio', '0052_procesosprocedimientospage_button_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestiondelainformacion',
            name='alt_text',
            field=models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo'),
        ),
        migrations.AddField(
            model_name='gestiondelainformacion',
            name='intro_title',
            field=models.CharField(default='Gestión de la Información', max_length=254, verbose_name='Título de la sección'),
        ),
        migrations.AlterField(
            model_name='gestiondelainformacion',
            name='elementos',
            field=wagtail.core.fields.StreamField([('Elementos', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Título que describe el elemento', label='Título del Elemento', required=True)), ('svg_image', wagtailsvg.blocks.SvgChooserBlock(help_text='Imagen', label='Imagen', required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ul', 'ol', 'italic', 'link', 'hr'], help_text='Texto descriptivo del elemento', icon='fa-paragraph', label='=Descripción', required=False, template='blocks/paragraph_block.html')), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local.', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa.Si este campo está completo, no se tendrá en cuenta el link a página local.', label='Link a página externa:', required=False))]))], blank=True, verbose_name='Adicione elementos informativos'),
        ),
        migrations.AlterField(
            model_name='gestiondelainformacion',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen'),
        ),
    ]
