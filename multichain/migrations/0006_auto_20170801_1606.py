# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 16:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multichain', '0005_test_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='send_coins',
            new_name='SendCoins',
        ),
        migrations.DeleteModel(
            name='Test_users',
        ),
    ]
