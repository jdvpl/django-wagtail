# Generated by Django 3.1.13 on 2021-11-11 20:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('ministerio', '0104_auto_20211111_1521'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistóricoPlaneacionEstratégicaSectorialPage',
            new_name='HistoricoPlaneacionEstrategicaSectorialPage',
        ),
    ]
