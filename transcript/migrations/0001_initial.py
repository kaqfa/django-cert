# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.DecimalField(max_digits=4, decimal_places=2)),
                ('status', models.CharField(default=b'0', max_length=2)),
                ('course', models.ForeignKey(to='department.Course')),
                ('student', models.ForeignKey(to='student.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
