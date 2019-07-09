<p>git clone https://github.com/AIDARXAN/mp3-video_converter</p>

<p>Make sure that celery and redis are properly installed on your PC</p>
    
    sudo apt-get install redis-server
If you want to check is redis-server working properly type command below

    redis-cli ping
    
It must return 'PONG'


    virtualenv mp3_env -p python3
    source mp3_env/bin/activate
    pip install -r requirements.txt

    python3 manage.py migrate <br>

Run server =>  

    python3 manage.py runserver
    
Run celery task manager =>
    
    celery -A AsyncVideoConverter worker -l info
