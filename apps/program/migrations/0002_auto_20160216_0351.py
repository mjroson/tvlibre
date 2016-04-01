# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program',
            options={'verbose_name': 'Program', 'ordering': ['title'], 'verbose_name_plural': 'Programs'},
        ),
    ]
