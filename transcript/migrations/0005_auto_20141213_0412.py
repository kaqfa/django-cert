# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0004_auto_20141213_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcript',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 4, 12, 16, 736588, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transcript',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 4, 12, 16, 736621, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
