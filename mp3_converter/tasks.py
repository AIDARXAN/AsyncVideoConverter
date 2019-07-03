import string
import youtube_dl

from django.core.mail import send_mail
from django.http import HttpResponse
from celery import Celery, shared_task
from AsyncVideoConverter.settings import *

app = Celery('tasks', broker=BROKER_URL)


@shared_task
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


@shared_task
def send_to_mail(mail, url):
    send_mail(
        # Email subject
        subject='Download link from Django server',
        # Email text
        message='Click on the link to download or listen to the video ' + url,
        # from email account
        from_email='mainwinnertactics@gmail.com',
        # to email account
        recipient_list=[mail],
        # bool => true or false, false means raise some exception, if occure
        fail_silently=False,
        )
