# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 20:53
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=versatileimagefield.fields.VersatileImageField(blank=True, default='avatar/profile/pdefault.jpg', upload_to='avatar/profile', verbose_name='Avatar'),
        ),
    ]
