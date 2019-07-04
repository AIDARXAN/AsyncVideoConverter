import string
import youtube_dl

from django.core.mail import send_mail
from django.http import HttpResponse
from celery import Celery, app
from AsyncVideoConverter.settings import EMAIL_HOST_USER, BROKER_URL

app = Celery('tasks', broker=BROKER_URL)


@app.task
def convert(mail, url, scheme, host):
    ydl_opts = {
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': 'media/%(id)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=True)
        audio_id = meta['id']
        link_download = scheme + '://' + host + '/media/' + id + '.mp3'
        send_to_mail.delay(mail, link_download)
        return meta['title']


@app.task
def send_to_mail(mail, url):
    send_mail(
        subject='Download link from Django server',
        message='Click on the link to download or listen to the mp3 ' + url,
        from_email=EMAIL_HOST_USER,
        recipient_list=[mail],
        fail_silently=False,
        )
