echo "sleep"
sleep 10

echo "make migrations"
python app/manage.py makemigrations

echo "migrate"
python app/manage.py migrate

echo "runserver"
python app/manage.py runserver 0.0.0.0:8000