# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0005_auto_20141213_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 5, 39, 42, 893608, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 5, 39, 42, 893641, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 5, 39, 42, 893608, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 5, 39, 42, 893641, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
