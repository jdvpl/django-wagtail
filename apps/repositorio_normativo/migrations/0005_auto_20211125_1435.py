# Generated by Django 3.1.13 on 2021-11-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0004_conceptopage_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptopage',
            name='norm_abolish',
            field=models.TextField(blank=True, help_text='Norma Derogada', verbose_name='Norma Derogada'),
        ),
    ]
