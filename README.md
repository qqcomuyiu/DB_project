(Based on linux)

To run this, first download django by:

sudo apt update

sudo apt install python3-pip (If you don't have python)

pip3 install django

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

Then:

python manage.py runserver

Visit http://127.0.0.1:8000/accounts/signup to register
and http://127.0.0.1:8000/accounts/login to login
and http://127.0.0.1:8000/admin to login the Django Admin Backend
