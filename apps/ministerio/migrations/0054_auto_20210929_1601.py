# Generated by Django 3.1.13 on 2021-09-29 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0053_auto_20210929_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gestiondelainformacion',
            old_name='elementos',
            new_name='elements',
        ),
    ]
