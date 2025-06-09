python -m venv .venv

cd .venv/scripts

activate

pip install django psycopg2 pillow

cd ../..

py manage.py makemigrations

py manage.py migrate

py manage.py createsuperuser

py manage.py runserver
