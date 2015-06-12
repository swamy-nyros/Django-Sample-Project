# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150518_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='uname',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
