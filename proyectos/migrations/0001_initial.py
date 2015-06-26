# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=80, verbose_name=b'Slug para las URLs de los proyectos')),
                ('nombre_proyecto', models.CharField(max_length=80, verbose_name=b'Nombre del proyecto')),
                ('descripcion_proyecto', models.TextField(verbose_name=b'Descripci\xc3\xb3n del proyecto')),
                ('lenguajes_utilizados', models.CharField(help_text=b'Ejemplo: Python, Javascript, Ruby, etc.', max_length=80, verbose_name=b'Lenguajes utilizados en el proyecto')),
                ('bases_de_datos', models.CharField(help_text=b'Ejemplo: MySQL, PostgreSQL, MongoDB, etc.', max_length=80, verbose_name=b'Bases de datos utilizadas en el proyecto')),
                ('frameworks_backend', models.CharField(help_text=b'Ejemplo: Django, Sails.js, Rails, etc.', max_length=80, verbose_name=b'Frameworks Backend utilizados en el proyecto (opcional)', blank=True)),
                ('frameworks_frontend', models.CharField(help_text=b'Ejemplo: Angular.js, Backbone.js, Bootstrap, etc.', max_length=80, verbose_name=b'Frameworks Frontend utilizados en el proyecto (opcional)', blank=True)),
                ('servidor_web', models.CharField(help_text=b'Ejemplo: Apache, Nginx, Unicorn, Tomcat, Gunicorn, etc.', max_length=50, verbose_name=b'Servidor web en el que corre el proyecto (opcional)', blank=True)),
                ('plugins_libs', models.TextField(help_text=b'Ejemplo: jQuery, React.js, Fancybox, jQuery UI, etc.', verbose_name=b'Plugins y librer\xc3\xadas utilizadas en el proyecto (opcional)', blank=True)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name=b'Fecha de creaci\xc3\xb3n')),
            ],
        ),
    ]
