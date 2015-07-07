# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0004_auto_20150627_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='nivel',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Nivel del m\xc3\xb3dulo'),
            preserve_default=False,
        ),
    ]
