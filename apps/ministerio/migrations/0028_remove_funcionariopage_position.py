# Generated by Django 3.1.7 on 2021-06-29 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0027_auto_20210629_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionariopage',
            name='position',
        ),
    ]
