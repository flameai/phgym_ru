# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0035_auto_20161201_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
