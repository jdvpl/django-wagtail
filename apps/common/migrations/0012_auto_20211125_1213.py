# Generated by Django 3.1.13 on 2021-11-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_ano'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ano',
            options={'verbose_name': 'Año', 'verbose_name_plural': 'Años'},
        ),
        migrations.AlterField(
            model_name='ano',
            name='year',
            field=models.IntegerField(verbose_name='Año concepto'),
        ),
    ]
