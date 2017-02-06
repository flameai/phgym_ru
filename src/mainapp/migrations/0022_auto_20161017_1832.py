# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 13:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_auto_20161017_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='dayclub',
            new_name='weekday',
        ),
        migrations.AlterUniqueTogether(
            name='entry',
            unique_together=set([('weekday', 'time')]),
        ),
    ]
