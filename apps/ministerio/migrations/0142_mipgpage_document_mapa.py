# Generated by Django 3.1.13 on 2021-11-22 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('ministerio', '0141_auto_20211122_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='mipgpage',
            name='document_mapa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document', verbose_name='Documento'),
        ),
    ]
