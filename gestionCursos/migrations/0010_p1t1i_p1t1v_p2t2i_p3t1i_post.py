# Generated by Django 3.2.5 on 2021-08-09 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionCursos', '0009_alter_curso_pendientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Nada', max_length=40)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionCursos.curso')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='P3T1I',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
                ('texto2', models.TextField()),
                ('texto3', models.TextField()),
                ('img1', models.ImageField(upload_to='')),
                ('Post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionCursos.post')),
            ],
            options={
                'verbose_name': 'Plantilla_P3T1I',
                'verbose_name_plural': 'Plantillas_P3T1I',
            },
        ),
        migrations.CreateModel(
            name='P2T2I',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
                ('texto2', models.TextField()),
                ('img1', models.ImageField(upload_to='')),
                ('img2', models.ImageField(upload_to='')),
                ('Post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionCursos.post')),
            ],
            options={
                'verbose_name': 'Plantilla_P2T2I',
                'verbose_name_plural': 'Plantillas_P2T2I',
            },
        ),
        migrations.CreateModel(
            name='P1T1V',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
                ('vid1', models.URLField(max_length=255)),
                ('Post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionCursos.post')),
            ],
            options={
                'verbose_name': 'Plantilla_P3T1I',
                'verbose_name_plural': 'Plantillas_P3T1I',
            },
        ),
        migrations.CreateModel(
            name='P1T1I',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
                ('img1', models.ImageField(upload_to='')),
                ('Post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionCursos.post')),
            ],
            options={
                'verbose_name': 'Plantilla_P1T1I',
                'verbose_name_plural': 'Plantillas_P1T1I',
            },
        ),
    ]
