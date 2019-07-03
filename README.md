<p>git clone https://github.com/AIDARXAN/mp3-video_converter</p>

virtualenv mp3_env -p python3
<br>
source mp3_env/bin/activate
<br>
pip install -r requirements.txt
<br>
in folder with settings.py create file secrets.py
<br>
and put SECRET_KEY="your_key"
<br>

python3 manage.py makemigrations<br>
python3 manage.py migrate <br>
python3 manage.py runserver<br>
