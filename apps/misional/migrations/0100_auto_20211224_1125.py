# Generated by Django 3.1.13 on 2021-12-24 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0099_reglamentotecnicoinstalacioneselectricaspage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reglamentotecnicoinstalacioneselectricaspage',
            name='alt_text',
        ),
        migrations.RemoveField(
            model_name='reglamentotecnicoinstalacioneselectricaspage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='reglamentotecnicoinstalacioneselectricaspage',
            name='intro',
        ),
        migrations.RemoveField(
            model_name='reglamentotecnicoinstalacioneselectricaspage',
            name='intro_title',
        ),
        migrations.RemoveField(
            model_name='reglamentotecnicoinstalacioneselectricaspage',
            name='link_video',
        ),
    ]