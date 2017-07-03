# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-03 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0085_auto_20170703_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='\u0441\u043a\u0440\u044b\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430'),
        ),
    ]
