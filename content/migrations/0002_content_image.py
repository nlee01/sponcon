# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.CharField(default='image-path-here', max_length=500),
            preserve_default=False,
        ),
    ]
