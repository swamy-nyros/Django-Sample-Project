# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20150603_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='upload_file',
            field=models.FileField(upload_to=b'upload_files/%Y/%m/%d'),
        ),
    ]
