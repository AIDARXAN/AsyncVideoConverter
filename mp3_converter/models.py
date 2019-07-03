from datetime import datetime
from django.db import models
from django.utils.timezone import get_current_timezone


class AudioFile(models.Model):
    url = models.URLField(max_length=1000)
    video_title = models.CharField(max_length=500, default="null")
    email = models.EmailField(max_length=50, default="null")
    request_sent = models.DateTimeField(default=datetime.now(tz=get_current_timezone()))

    def __str__(self):
        return "(%s, %s, %s)" % (self.url, self.video_title, self.email)
