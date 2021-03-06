# Generated by Django 3.2.5 on 2021-08-09 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionCursos', '0011_auto_20210809_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='P2T1I',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
                ('texto2', models.TextField()),
                ('img1', models.ImageField(upload_to='img1_P2T1I')),
                ('Post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionCursos.post')),
            ],
            options={
                'verbose_name': 'Plantilla_P2T1I',
                'verbose_name_plural': 'Plantillas_P2T1I',
            },
        ),
    ]
