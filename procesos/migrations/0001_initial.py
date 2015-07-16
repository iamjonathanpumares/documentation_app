# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0001_initial'),
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
                ('modulo', models.ForeignKey(related_name='actividades', blank=True, to='documentacion.Modulo', null=True)),
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
        migrations.AddField(
            model_name='actividad',
            name='proceso',
            field=models.ForeignKey(related_name='actividades', to='procesos.Proceso'),
        ),
    ]
