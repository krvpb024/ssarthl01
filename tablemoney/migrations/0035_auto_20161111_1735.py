# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-11 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0034_auto_20161111_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablemoney',
            name='workday_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]