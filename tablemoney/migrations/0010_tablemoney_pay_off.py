# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-05 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0009_auto_20161105_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablemoney',
            name='pay_off',
            field=models.BooleanField(default=False),
        ),
    ]