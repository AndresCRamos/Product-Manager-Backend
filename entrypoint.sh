#!/bin/bash
echo "Searching for DB"

while ! nc -z db 5432; do
    echo "Waiting for DB..."
    sleep 3
  done
echo "DB found"

sleep 3

echo "activate venv"
source venv/bin/activate

echo "make migrations"
python app/manage.py makemigrations

echo "migrate"
python app/manage.py migrate

echo "create views"
python app/manage.py createviewtable

echo "runserver"
python app/manage.py runserver 0.0.0.0:8000
