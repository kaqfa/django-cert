# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20141213_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 4, 10, 1, 846186, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='graduation',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 4, 10, 1, 846223, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 4, 10, 1, 846186, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.PositiveSmallIntegerField(default=3, choices=[(1, b'Aktif'), (2, b'Non Aktif'), (3, b'Mangkir'), (4, b'Lulus'), (5, b'Meninggal')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 4, 10, 1, 846223, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
