# -*- coding: utf-8 -*-
# Generated by Django 1.9.5.dev20160312175816 on 2016-03-16 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_medicines_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicines',
            name='refill',
            field=models.BooleanField(default=True),
        ),
    ]
