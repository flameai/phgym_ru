# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-21 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0063_auto_20170221_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short_text',
            field=models.TextField(default=b'', max_length=210, verbose_name='\u043a\u0440\u0430\u0442\u043a\u0438\u0439 \u0442\u0435\u043a\u0441\u0442 \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='short_text',
            field=models.TextField(default=b'', max_length=210, verbose_name='\u043a\u0440\u0430\u0442\u043a\u0438\u0439 \u0442\u0435\u043a\u0441\u0442'),
        ),
    ]
