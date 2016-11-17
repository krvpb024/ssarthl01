# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-06 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20161105_0331'),
        ('tablemoney', '0015_month_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablemoney',
            name='pay_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='tablemoney',
            name='payee',
            field=models.ManyToManyField(to='userprofile.UserProfile'),
        ),
        migrations.AlterField(
            model_name='tablemoney',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payer', to='userprofile.UserProfile'),
        ),
    ]