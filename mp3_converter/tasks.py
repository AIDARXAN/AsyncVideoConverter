import string
import youtube_dl

from django.core.mail import send_mail
from django.http import HttpResponse
from celery import Celery, app
from AsyncVideoConverter.settings import *
from AsyncVideoConverter.settings import EMAIL_HOST_USER
app = Celery('tasks', broker=BROKER_URL)


@app.task
def convert(mail, url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)
        send_to_mail.delay(mail, meta['url'])
        return meta['title']


@app.task
def send_to_mail(mail, url):
    send_mail(
        # Email subject
        subject='Download link from Django server',
        # Email text
        message='Click on the link to download or listen to the video ' + url,
        # from email account
        from_email=EMAIL_HOST_USER,
        # to email account
        recipient_list=[mail],
        # bool => true or false, false means raise some exception, if occure
        fail_silently=False,
        )
