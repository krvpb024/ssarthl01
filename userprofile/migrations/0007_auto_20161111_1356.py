# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-11 05:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_userprofile_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['number']},
        ),
    ]