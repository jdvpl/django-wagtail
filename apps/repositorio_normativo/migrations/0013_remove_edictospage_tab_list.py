# Generated by Django 3.1.13 on 2022-02-26 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0012_edictospage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edictospage',
            name='tab_list',
        ),
    ]