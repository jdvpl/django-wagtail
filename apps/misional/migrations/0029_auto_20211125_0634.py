# Generated by Django 3.1.13 on 2021-11-25 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0028_auto_20211125_0629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudadesenergeticaspage',
            old_name='link_list',
            new_name='city_list',
        ),
    ]