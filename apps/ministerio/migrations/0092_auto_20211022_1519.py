# Generated by Django 3.1.13 on 2021-10-22 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0091_auto_20211022_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contratacionpage',
            old_name='link_externo',
            new_name='external_link',
        ),
    ]
