# Generated by Django 3.1.13 on 2022-04-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0169_auto_20220412_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionariopage',
            name='position',
            field=models.CharField(blank=True, help_text='Cargo del funcionario.', max_length=255, null=True, verbose_name='Cargo del funcionario'),
        ),
    ]
