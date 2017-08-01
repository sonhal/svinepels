# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 14:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multichain', '0002_auto_20170729_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_addresses',
            name='name',
            field=models.CharField(default='Gaddeveien Beboer', max_length=100),
        ),
        migrations.AlterField(
            model_name='user_addresses',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blockchain_address', to=settings.AUTH_USER_MODEL),
        ),
    ]
