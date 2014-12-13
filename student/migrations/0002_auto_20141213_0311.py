# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='graduation',
            options={'verbose_name': 'Periode Wisuda', 'verbose_name_plural': 'Periode Wisuda'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Mahasiswa', 'verbose_name_plural': 'Mahasiswa'},
        ),
    ]
