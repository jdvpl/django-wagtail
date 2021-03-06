# Generated by Django 3.1.13 on 2021-11-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0031_auto_20211128_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='energiapage',
            name='latitude',
            field=models.FloatField(blank=True, default=0, help_text='Latitud, valores entre -90 y 90', verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='energiapage',
            name='longitude',
            field=models.FloatField(blank=True, default=0, help_text='Longitud, valores entre -180 y 180', verbose_name='Longitud'),
        ),
    ]
