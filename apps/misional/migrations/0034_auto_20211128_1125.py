# Generated by Django 3.1.13 on 2021-11-28 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailsvg', '0002_svg_edit_code'),
        ('misional', '0033_auto_20211128_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='energiaindexpage',
            name='alt_text',
            field=models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo de la imagen'),
        ),
        migrations.AddField(
            model_name='energiaindexpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='energiaindexpage',
            name='intro',
            field=models.TextField(blank=True, help_text='Introducción', null=True, verbose_name='Introducción'),
        ),
        migrations.AddField(
            model_name='energiaindexpage',
            name='link_video',
            field=models.URLField(blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', verbose_name='Video'),
        ),
        migrations.AddField(
            model_name='energiaindexpage',
            name='projects',
            field=models.TextField(blank=True, help_text='Proyectos', verbose_name='Proyectos'),
        ),
        migrations.AddField(
            model_name='energiaindexpage',
            name='users',
            field=models.TextField(blank=True, help_text='Usuarios', verbose_name='Usuarios'),
        ),
        migrations.AlterField(
            model_name='energiapage',
            name='alt_text',
            field=models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo de la imagen'),
        ),
        migrations.AlterField(
            model_name='energiapage',
            name='icon',
            field=models.ForeignKey(help_text='Icono del tipo de energía', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailsvg.svg', verbose_name='Icono del tipo de energía'),
        ),
    ]
