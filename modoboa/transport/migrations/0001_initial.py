# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-24 11:16
from __future__ import unicode_literals

from django.db import migrations, models

import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(max_length=254, unique=True, verbose_name='pattern')),
                ('service', models.CharField(max_length=30, verbose_name='service')),
                ('next_hop', models.CharField(blank=True, max_length=100, verbose_name='next hop')),
                ('_settings', jsonfield.fields.JSONField(default={})),
            ],
            options={
                'ordering': ['pattern'],
            },
        ),
    ]
