# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_actividad', models.CharField(max_length=150, verbose_name=b'Nombre de la actividad')),
                ('tipo_actividad', models.CharField(max_length=1, verbose_name=b'Tipo de actividad', choices=[(b'E', b'Entrada'), (b'P', b'Proceso'), (b'D', b'Decisi\xc3\xb3n'), (b'S', b'Salida')])),
                ('orden', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_proceso', models.CharField(max_length=50, verbose_name=b'Nombre del proceso')),
                ('descripcion_proceso', models.TextField(verbose_name=b'Descripci\xc3\xb3n del proceso')),
                ('proyecto', models.ForeignKey(related_name='procesos', to='proyectos.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('responsable', models.CharField(max_length=50, verbose_name=b'Responsable involucrado en el proceso')),
                ('proceso', models.ForeignKey(related_name='responsables', to='procesos.Proceso')),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='proceso',
            field=models.ForeignKey(related_name='actividades', to='procesos.Proceso'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='responsable',
            field=models.ForeignKey(related_name='actividades', to='procesos.Responsable'),
        ),
    ]
