# Generated by Django 3.1.13 on 2021-11-18 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211117_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='systems_title',
            field=models.CharField(blank=True, help_text='Título del la sección', max_length=120, null=True, verbose_name='Título del la sección'),
        ),
    ]
