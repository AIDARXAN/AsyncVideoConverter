# Generated by Django 2.2.2 on 2019-07-08 00:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mp3_converter', '0004_auto_20190626_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiofile',
            name='video_title',
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='request_sent',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 8, 0, 51, 39, 412801, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='url',
            field=models.URLField(),
        ),
    ]
