# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-06 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0020_year_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tablemoney',
            name='year',
        ),
        migrations.AlterField(
            model_name='month',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]