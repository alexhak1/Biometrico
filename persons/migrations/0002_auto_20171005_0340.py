# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='personid',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
