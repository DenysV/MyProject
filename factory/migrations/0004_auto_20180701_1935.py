# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0003_auto_20180701_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
