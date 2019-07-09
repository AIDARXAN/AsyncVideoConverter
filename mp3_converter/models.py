from django.db import models


class AudioFile(models.Model):
    url = models.URLField(max_length=200)
    email = models.EmailField(max_length=50, default="null")
    request_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "(%s)" % self.url
