# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-04 13:43
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0089_auto_20170704_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0448\u0430\u0431\u043b\u043e\u043d \u0437\u0430\u043d\u044f\u0442\u0438\u044f',
                'verbose_name_plural': '\u0448\u0430\u0431\u043b\u043e\u043d\u044b \u0437\u0430\u043d\u044f\u0442\u0438\u0439',
            },
        ),
        migrations.RemoveField(
            model_name='entry',
            name='description',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='image',
        ),
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='mainapp.EntryTemplate', verbose_name='\u0417\u0430\u043d\u044f\u0442\u0438\u0435'),
        ),
    ]
