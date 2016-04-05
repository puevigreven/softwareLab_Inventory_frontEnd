# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-04 16:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharma',
            name='Password',
            field=models.TextField(default=datetime.datetime(2016, 4, 4, 16, 46, 11, 868420, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharma',
            name='User_ID',
            field=models.TextField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]
