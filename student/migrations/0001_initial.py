# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graduation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', models.IntegerField()),
                ('grad_date', models.DateField()),
                ('venue', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('nim', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(default=b'', max_length=200, blank=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.CharField(max_length=200, null=True, blank=True)),
                ('status', models.CharField(default=b'1', max_length=2, choices=[(b'1', b'Aktif'), (b'2', b'Non Aktif')])),
                ('graduation', models.ForeignKey(blank=True, to='student.Graduation', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
