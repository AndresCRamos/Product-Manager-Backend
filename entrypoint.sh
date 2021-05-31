echo "sleep"
sleep 10

echo "create venv"
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

echo "make migrations"
python app/manage.py makemigrations

echo "migrate"
python app/manage.py migrate

echo "create views"
python app/manage.py createviewtable

echo "runserver"
python app/manage.py runserver 0.0.0.0:8000