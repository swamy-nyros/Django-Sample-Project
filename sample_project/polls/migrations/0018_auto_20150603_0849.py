# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20150603_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='upload_file',
            field=models.FileField(upload_to=b'upload_files'),
        ),
    ]
