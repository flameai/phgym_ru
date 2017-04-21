# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-21 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0074_auto_20170419_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
            ],
            options={
                'verbose_name': '\u043e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u043e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f',
            },
        ),
        migrations.AlterField(
            model_name='form',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Club', verbose_name='\u041a\u043b\u0443\u0431'),
        ),
    ]
