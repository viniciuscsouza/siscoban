# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171129_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='user',
        ),
    ]