echo "wait for database"
nc -z db 5432
x=$?
while [ $x -ne 0 ]
do
  echo "waiting for db"
  nc -z db 5432>/dev/null
  x=$?
  sleep 1
done
echo "found db"

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