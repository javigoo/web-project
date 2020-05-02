@echo off
cd ..\..\
venv\Scripts\activate && python manage.py migrate && python manage.py runserver
exit