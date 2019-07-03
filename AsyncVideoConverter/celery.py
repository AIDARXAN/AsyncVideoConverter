from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AsyncVideoConverter.settings')

app = Celery('AsyncVideoConverter',
             backend=settings.RESULT_BACKEND,
             broker=settings.BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


if __name__ == '__main__':
    app.start()
