# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-17 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0078_auto_20170517_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='emails_send',
            field=models.CharField(default=b'', help_text='\u041c\u043e\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e.', max_length=200, verbose_name='E-\u043c\u0430\u0439\u043b \u0434\u043b\u044f \u0437\u0430\u044f\u0432\u043e\u043a'),
        ),
    ]
