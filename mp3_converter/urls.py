from django.urls import path
from . import views

app_name = "mp3_converter"
urlpatterns = [
     path('', views.index, name='index'),
]
