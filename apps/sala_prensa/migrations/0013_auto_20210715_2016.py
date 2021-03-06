# Generated by Django 3.1.7 on 2021-07-16 01:16

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        ('sala_prensa', '0012_auto_20210715_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_title', models.CharField(max_length=254, verbose_name='Nombre del sector')),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectores',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.AlterField(
            model_name='noticiapage',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ciudad'),
        ),
        migrations.CreateModel(
            name='NoticiaSectorRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_noticia_relationship', to='sala_prensa.sector')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='noticia_sector_relationship', to='sala_prensa.noticiapage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
