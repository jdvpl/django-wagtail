# Generated by Django 3.1.7 on 2021-05-12 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0016_auto_20210423_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estructurasectorpage',
            name='related_entities',
        ),
        migrations.RemoveField(
            model_name='estructurasectorpage',
            name='sector_entities',
        ),
    ]
