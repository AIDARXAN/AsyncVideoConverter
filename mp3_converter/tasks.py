import youtube_dl

from django.core.mail import send_mail
from celery import Celery
from django.conf import settings

app = Celery('tasks', broker=settings.BROKER_URL)


@app.task
def convert(mail, url, protocol, host):
    ydl_opts = {
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': 'audio/%(id)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=True)
        audio_id = meta['id']
        download_link = protocol + '://' + host + '/media/' + audio_id + '.mp3'
        send_to_mail.delay(mail, download_link)


@app.task
def send_to_mail(mail, url):
    send_mail(subject='Download link from Django server',
              message='Click on the link to download or listen to the mp3 ' + url,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[mail],        
              fail_silently=False,)
