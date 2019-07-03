from __future__ import unicode_literals


from .forms import DownloadForm
from .models import AudioFile
from django.shortcuts import render
from .tasks import *
from django.http import HttpResponse
from json import JSONEncoder


def index(request):
    form = DownloadForm()
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            url   = form.cleaned_data.get('url')
            email = form.cleaned_data.get('email')
            meta  = convert.delay(url)
            meta.ready()
            send_mail = send_to_mail.apply_async((email, meta), serializer='json')
            send_mail.ready()
            audio_file = AudioFile.objects.create(url=url, email=email)
            audio_file.save()
            return HttpResponse('%s' % send_mail)    

    return render(request, "mp3_converter/index.html", context={'form': form})
