# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20161129_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imagefile',
            field=models.ImageField(default='none', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]