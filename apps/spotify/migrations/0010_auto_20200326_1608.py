# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0009_auto_20200325_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='song',
            new_name='songs',
        ),
        migrations.RemoveField(
            model_name='spotify_user',
            name='id',
        ),
        migrations.AlterField(
            model_name='playlist',
            name='id',
            field=models.CharField(primary_key=True, max_length=200, serialize=False),
        ),
        migrations.AlterField(
            model_name='spotify_user',
            name='name',
            field=models.CharField(primary_key=True, max_length=30, default=datetime.datetime(2020, 3, 26, 16, 8, 41, 897455, tzinfo=utc), serialize=False),
            preserve_default=False,
        ),
    ]
