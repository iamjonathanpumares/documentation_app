# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campo', models.CharField(max_length=35, verbose_name=b'Campo de la tabla')),
                ('longitud', models.PositiveSmallIntegerField(verbose_name=b'Longitud del campo')),
                ('tipo_dato', models.CharField(max_length=35, verbose_name=b'Tipo de dato del campo')),
                ('descripcion', models.CharField(max_length=100, verbose_name=b'Descripci\xc3\xb3n del campo')),
                ('campo_clave', models.BooleanField(verbose_name=b'Campo clave')),
            ],
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campo', models.ForeignKey(related_name='relaciones', to='diccionario_de_datos.Campo')),
            ],
        ),
        migrations.CreateModel(
            name='Tabla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_tabla', models.CharField(max_length=35, verbose_name=b'Nombre de la tabla')),
                ('descripcion_tabla', models.CharField(max_length=150, verbose_name=b'Descripci\xc3\xb3n de la tabla')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name=b'Fecha de creaci\xc3\xb3n')),
                ('proyecto', models.ForeignKey(related_name='tablas', to='proyectos.Proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='relacion',
            name='tabla_referencia',
            field=models.ForeignKey(related_name='relaciones', to='diccionario_de_datos.Tabla'),
        ),
        migrations.AddField(
            model_name='campo',
            name='tabla',
            field=models.ForeignKey(related_name='campos', to='diccionario_de_datos.Tabla'),
        ),
    ]
