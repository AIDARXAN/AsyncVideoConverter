<p>git clone https://github.com/AIDARXAN/mp3-video_converter</p>

<p>Make sure that celery and redis are properly installed on your PC</p>
<p>sudo apt-get install redis-server</p>
If you want to check is redis-server working properly type command below
<p>redis-cli ping</p>
It must return 'PONG'

<br>
virtualenv mp3_env -p python3
<br>
source mp3_env/bin/activate
<br>
pip install -r requirements.txt
<br>


python3 manage.py migrate <br>

Run server => python3 manage.py runserver<br>
Run celery task manager => celery -A AsyncVideoConverter worker -l info