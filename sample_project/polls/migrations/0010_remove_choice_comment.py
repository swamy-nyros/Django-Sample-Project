# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20150518_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='comment',
        ),
    ]
