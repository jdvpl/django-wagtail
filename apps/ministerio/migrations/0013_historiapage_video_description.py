# Generated by Django 3.1.7 on 2021-04-22 14:42

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0012_auto_20210422_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiapage',
            name='video_description',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Descripción del video', null=True),
        ),
    ]
