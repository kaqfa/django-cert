# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0003_auto_20141213_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 4, 10, 1, 846186, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='certificate',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 4, 10, 1, 846223, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legalization',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 4, 10, 1, 846186, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legalization',
            name='status',
            field=models.PositiveSmallIntegerField(default=2, choices=[(1, b'Verified'), (2, b'In Progress'), (3, b'Invalid')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legalization',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 4, 10, 1, 846223, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
