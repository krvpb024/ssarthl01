# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-25 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0005_auto_20161225_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhuditable',
            name='session',
            field=models.CharField(max_length=50),
        ),
    ]
