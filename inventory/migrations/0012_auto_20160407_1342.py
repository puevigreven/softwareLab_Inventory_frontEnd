# -*- coding: utf-8 -*-
# Generated by Django 1.9.5.dev20160312175816 on 2016-04-07 13:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20160407_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='expiry_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]