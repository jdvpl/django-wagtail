# Generated by Django 3.1.13 on 2022-04-06 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0136_conoceunidadresultadospage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidadresultadospage',
            name='button_title',
        ),
        migrations.RemoveField(
            model_name='unidadresultadospage',
            name='document_mapa',
        ),
        migrations.RemoveField(
            model_name='unidadresultadospage',
            name='link_mapa',
        ),
    ]
