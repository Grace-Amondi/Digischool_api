# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_issue_when'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='when',
            new_name='date',
        ),
    ]
