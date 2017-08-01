# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 14:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('multichain', '0003_auto_20170729_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='send_coins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sendt_coins', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_coins', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]