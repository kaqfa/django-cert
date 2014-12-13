# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name=b'Kode Mata Kuliah')),
                ('name', models.CharField(max_length=100, verbose_name=b'Nama Mata Kuliah')),
                ('status', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Aktif'), (b'0', b'Non Aktif')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50, verbose_name=b'Program Studi')),
                ('faculty', models.CharField(max_length=80, verbose_name=b'Fakultas')),
                ('status', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Aktif'), (b'0', b'Non Aktif')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(verbose_name=b'Fakultas', to='department.Department'),
            preserve_default=True,
        ),
    ]
