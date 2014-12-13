# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0002_auto_20141213_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 3, 38, 34, 680054, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='certificate',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 3, 38, 34, 680087, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legalization',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 3, 38, 34, 680054, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legalization',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 3, 38, 34, 680087, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
