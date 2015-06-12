# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20150518_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='question_id',
            new_name='question',
        ),
    ]
