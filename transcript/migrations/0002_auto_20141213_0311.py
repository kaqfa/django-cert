# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transcript',
            options={'verbose_name': 'Transkrip Nilai', 'verbose_name_plural': 'Transkrip Nilai'},
        ),
    ]
