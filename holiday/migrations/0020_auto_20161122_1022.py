# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-22 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0019_holiday_identify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holiday',
            name='date',
        ),
        migrations.AddField(
            model_name='holiday',
            name='date',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]