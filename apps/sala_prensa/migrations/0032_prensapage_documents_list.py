# Generated by Django 3.1.7 on 2021-08-02 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('sala_prensa', '0031_auto_20210802_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='prensapage',
            name='documents_list',
            field=models.ForeignKey(blank=True, help_text='Seleccione la página del índice de documentos', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Índice de documentos'),
        ),
    ]
