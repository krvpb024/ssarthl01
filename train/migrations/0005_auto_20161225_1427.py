# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-25 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0004_auto_20161225_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zuxuntable',
            name='session',
        ),
        migrations.AddField(
            model_name='zuxuntable',
            name='session',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]