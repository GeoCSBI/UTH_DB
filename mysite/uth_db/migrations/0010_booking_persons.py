# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uth_db', '0009_auto_20170102_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='persons',
            field=models.IntegerField(null=True),
        ),
    ]
