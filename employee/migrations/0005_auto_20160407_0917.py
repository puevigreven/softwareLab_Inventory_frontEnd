# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-07 09:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Employee_ID',
            new_name='Patient_ID',
        ),
        migrations.AddField(
            model_name='employee',
            name='Date_Of_Upload',
            field=models.DateField(default=datetime.datetime(2016, 4, 7, 9, 17, 29, 962707, tzinfo=utc)),
            preserve_default=False,
        ),
    ]