# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_obs',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
