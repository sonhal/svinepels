# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multichain', '0008_remove_sendcoins_from_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendcoins',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
