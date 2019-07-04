from __future__ import unicode_literals


from .forms import DownloadForm
from .models import AudioFile
from .tasks import convert
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.mail import send_mail


@ensure_csrf_cookie
def index(request):
    form = DownloadForm()
    if request.method == 'POST':
        form = DownloadForm(request.POST or None)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            email = form.cleaned_data.get('email')
            
            title = convert.delay(email, url, request.scheme, request.META['HTTP_HOST'])

            audio_file = AudioFile.objects.create(url=url, email=email, video_title=title)
            audio_file.save()

            return redirect('/')
    return render(request, "mp3_converter/index.html", context={'form': form})
