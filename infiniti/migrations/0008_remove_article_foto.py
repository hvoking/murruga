# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infiniti', '0007_auto_20170319_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='foto',
        ),
    ]