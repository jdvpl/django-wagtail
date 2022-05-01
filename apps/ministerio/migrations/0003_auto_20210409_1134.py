# Generated by Django 3.1.7 on 2021-04-09 16:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('ministerio', '0002_contrataciopage_controlinternopage_entescontrolexternopage_estructuraorganizacionalpage_historiapage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContratacioPage',
            new_name='ContratacionPage',
        ),
    ]
