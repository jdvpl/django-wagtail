# Generated by Django 3.1.13 on 2021-12-04 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0061_downstreampage_systems_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='downstreampage',
            name='plan_title',
            field=models.CharField(default='Plan de abastecimiento', max_length=254, verbose_name='Título de la sección'),
        ),
    ]
