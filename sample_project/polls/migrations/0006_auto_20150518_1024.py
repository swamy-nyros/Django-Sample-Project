# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_comment_uname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='uname',
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
