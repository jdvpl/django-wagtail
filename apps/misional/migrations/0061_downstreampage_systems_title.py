# Generated by Django 3.1.13 on 2021-12-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0060_downstreampage'),
    ]

    operations = [
        migrations.AddField(
            model_name='downstreampage',
            name='systems_title',
            field=models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección'),
        ),
    ]
