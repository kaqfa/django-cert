# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Mata Kuliah', 'verbose_name_plural': 'Mata Kuliah'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Program Studi', 'verbose_name_plural': 'Program Studi'},
        ),
    ]
