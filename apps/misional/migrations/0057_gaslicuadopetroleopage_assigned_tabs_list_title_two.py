# Generated by Django 3.1.13 on 2021-12-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0056_gaslicuadopetroleopage'),
    ]

    operations = [
        migrations.AddField(
            model_name='gaslicuadopetroleopage',
            name='assigned_tabs_list_title_two',
            field=models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección'),
        ),
    ]
