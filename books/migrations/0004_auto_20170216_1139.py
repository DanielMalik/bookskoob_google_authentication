# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20170216_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='date_get',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logs',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
