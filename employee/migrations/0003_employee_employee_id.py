# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-04 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20160404_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Employee_ID',
            field=models.TextField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]
