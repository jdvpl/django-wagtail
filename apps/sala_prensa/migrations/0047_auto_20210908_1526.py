# Generated by Django 3.1.13 on 2021-09-08 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_autor_sector'),
        ('sala_prensa', '0046_auto_20210905_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audioautorrelationship',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_audio_relationship', to='common.autor'),
        ),
        migrations.AlterField(
            model_name='audiosectorrelationship',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_audio_relationship', to='common.sector'),
        ),
        migrations.AlterField(
            model_name='documentoautorrelationship',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_socumento_relationship', to='common.autor'),
        ),
        migrations.AlterField(
            model_name='documentosectorrelationship',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_documento_relationship', to='common.sector'),
        ),
        migrations.AlterField(
            model_name='eventoautorrelationship',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_evento_relationship', to='common.autor'),
        ),
        migrations.AlterField(
            model_name='eventosectorrelationship',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_evento_relationship', to='common.sector'),
        ),
        migrations.AlterField(
            model_name='galeriaautorrelationship',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_galeria_relationship', to='common.autor'),
        ),
        migrations.AlterField(
            model_name='galeriasectorrelationship',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_galeria_relationship', to='common.sector'),
        ),
        migrations.AlterField(
            model_name='infografiaautorrelationship',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_infografia_relationship', to='common.autor'),
        ),
        migrations.AlterField(
            model_name='infografiasectorrelationship',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_infografia_relationship', to='common.sector'),
        ),
        migrations.AlterField(
            model_name='noticiaautorrelationship',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_noticia_relationship', to='common.autor'),
        ),
        migrations.AlterField(
            model_name='noticiasectorrelationship',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_noticia_relationship', to='common.sector'),
        ),
        migrations.AlterField(
            model_name='videosautorrelationship',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_videos_relationship', to='common.autor'),
        ),
        migrations.AlterField(
            model_name='videossectorrelationship',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_videos_relationship', to='common.sector'),
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Sector',
        ),
    ]
