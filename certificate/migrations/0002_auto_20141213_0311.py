# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'verbose_name': 'Ijazah', 'verbose_name_plural': 'Ijazah'},
        ),
        migrations.AlterModelOptions(
            name='legalization',
            options={'verbose_name': 'Legalisir', 'verbose_name_plural': 'Legalisir'},
        ),
        migrations.AddField(
            model_name='legalization',
            name='submitter',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
