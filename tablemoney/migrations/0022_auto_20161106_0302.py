# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-06 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablemoney', '0021_auto_20161106_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='month',
            field=models.CharField(choices=[('11', '一月'), ('2', '二月'), ('3', '三月'), ('4', '四月'), ('5', '五月'), ('6', '六月'), ('7', '七月'), ('8', '八月'), ('9', '九月'), ('10', '十月'), ('11', '十一月'), ('12', '十二月')], max_length=20),
        ),
    ]