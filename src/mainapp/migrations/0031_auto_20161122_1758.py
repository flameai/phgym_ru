# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0030_merge_20161119_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='pagetype',
            field=models.CharField(choices=[('stock', 'Акции'), ('fitness', 'Top Fitness'), ('service', 'Услуги')], default='', max_length=10, verbose_name='Тип страницы'),
        ),
    ]
