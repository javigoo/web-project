@echo off
cd ..\..\
python -m venv venv && venv\Scripts\activate && pip3 install -r requirements.txt
python manage.py makemigrations && python manage.py migrate && python manage.py runserver
python manage.py test apps.spotify.test
exit