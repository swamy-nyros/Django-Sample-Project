# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_remove_file_upload_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='upload_file',
            field=models.FileField(upload_to=b'sample_project/polls/upload_files/%Y/%m/%d'),
        ),
    ]
