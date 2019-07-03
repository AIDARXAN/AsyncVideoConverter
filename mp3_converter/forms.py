from django import forms


class DownloadForm(forms.Form):
    url = forms.RegexField(
        regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$',
        max_length=300,
        label="Video Url")
    email = forms.EmailField(max_length=60, label="Your Email")
