# Generated by Django 3.1.13 on 2021-11-13 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0128_auto_20211113_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='politicasobjetivoscalidadlpage',
            old_name='risk_main_intro',
            new_name='risk_block_one',
        ),
        migrations.RenameField(
            model_name='politicasobjetivoscalidadlpage',
            old_name='risk_second_intro',
            new_name='risk_block_two',
        ),
    ]