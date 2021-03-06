# Generated by Django 3.1.13 on 2021-09-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_prensa', '0045_auto_20210904_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiopage',
            name='introduction',
            field=models.TextField(help_text='Texto que describe el audio', verbose_name='Introducción'),
        ),
        migrations.AlterField(
            model_name='documentopage',
            name='introduction',
            field=models.TextField(help_text='Texto que describe el documento', verbose_name='Introducción'),
        ),
        migrations.AlterField(
            model_name='videospage',
            name='introduction',
            field=models.TextField(help_text='Texto que describe el video', verbose_name='Introducción'),
        ),
    ]
