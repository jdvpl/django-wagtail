# Generated by Django 3.1.13 on 2021-12-02 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0047_auto_20211201_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='hidrocarburospage',
            name='link_pbi_six',
            field=models.URLField(blank=True, help_text='Link de acceso al tablero Power BI', verbose_name='Link tablero Power BI'),
        ),
        migrations.AlterField(
            model_name='hidrocarburospage',
            name='title_pbi',
            field=models.CharField(default='Información a publicar PPIS- GAS- Precios', max_length=254, verbose_name='Título de la sección'),
        ),
    ]
