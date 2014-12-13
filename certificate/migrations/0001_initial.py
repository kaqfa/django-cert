# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('certificate_number', models.CharField(max_length=25)),
                ('gpa', models.DecimalField(null=True, max_digits=3, decimal_places=2, blank=True)),
                ('student_nim', models.CharField(max_length=25, null=True, blank=True)),
                ('thesis_title', models.TextField(blank=True)),
                ('certificate_file', models.FileField(null=True, upload_to=b'certs_file', blank=True)),
                ('transcript1_file', models.FileField(null=True, upload_to=b'certs_file', blank=True)),
                ('transcript2_file', models.FileField(null=True, upload_to=b'certs_file', blank=True)),
                ('student', models.ForeignKey(to='student.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Legalization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uploaded_file', models.FileField(null=True, upload_to=b'legalize_file', blank=True)),
                ('qr_code', models.CharField(max_length=200)),
                ('submitted_at', models.DateTimeField()),
                ('status', models.CharField(max_length=1, choices=[(b'1', b'Verified'), (b'2', b'In Progress'), (b'3', b'Invalid')])),
                ('student', models.ForeignKey(blank=True, to='student.Student', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
