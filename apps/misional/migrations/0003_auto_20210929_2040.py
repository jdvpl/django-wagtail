# Generated by Django 3.1.13 on 2021-09-30 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0002_remove_misionalpage_link_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='misionalpage',
            name='intro_title',
            field=models.CharField(default='Misional', max_length=254, verbose_name='Título de la sección'),
        ),
    ]
