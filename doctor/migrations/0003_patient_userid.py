# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_patient_doctor_visited_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='UserID',
            field=models.TextField(default='s0'),
        ),
    ]
