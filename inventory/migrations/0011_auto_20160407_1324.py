# -*- coding: utf-8 -*-
# Generated by Django 1.9.5.dev20160312175816 on 2016-04-07 13:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20160407_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicines',
            name='batch_number',
            field=models.TextField(default=datetime.datetime(2016, 4, 7, 13, 24, 22, 481538, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicines',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicines',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
