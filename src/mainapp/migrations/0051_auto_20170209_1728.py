# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-09 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0050_stock_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='lat',
            field=models.FloatField(default=0.0, verbose_name='\u0448\u0438\u0440\u043e\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='club',
            name='lon',
            field=models.FloatField(default=0.0, verbose_name='\u0434\u043e\u043b\u0433\u043e\u0442\u0430'),
        ),
    ]
