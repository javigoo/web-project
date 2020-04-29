#!/usr/bin/sh
rm -rf web-project/
git clone https://github.com/Javigoo/web-project.git
cd ~/web-project/
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
(sleep 5 && xdg-open http://127.0.0.1:8000/) &
python3 manage.py runserver
