# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infiniti', '0006_article_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='/principal/static/imagens/'),
        ),
    ]