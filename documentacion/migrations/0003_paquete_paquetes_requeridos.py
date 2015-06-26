# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0002_auto_20150623_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='paquetes_requeridos',
            field=models.ManyToManyField(related_name='paquetes_requeridos_rel_+', to='documentacion.Paquete'),
        ),
    ]
