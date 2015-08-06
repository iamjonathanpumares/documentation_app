# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rol', models.CharField(help_text=b'Un rol son los distintos usuarios que interactuan con el sistema. Ejemplo: Gerente de ventas, el cliente, proveedor, empleado, recepcionista, etc.', max_length=50, verbose_name=b'Rol del actor')),
                ('proyecto', models.ForeignKey(related_name='actores', to='proyectos.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(verbose_name=b'Descripci\xc3\xb3n de la tarea o actividad que realiza el actor')),
                ('actor', models.ForeignKey(related_name='tareas', to='casos_de_uso.Actor')),
            ],
        ),
    ]
