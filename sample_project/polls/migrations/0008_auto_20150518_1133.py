# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150518_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='question_id',
            field=models.ForeignKey(to='polls.Question'),
        ),
    ]
