# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-05 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0002_auto_20161105_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablemoney',
            name='day_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablemoney',
            name='holiday_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tablemoney',
            name='totle_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]