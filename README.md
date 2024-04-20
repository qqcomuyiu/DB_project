(Based on linux)

To run this, first download django by:
```
sudo apt update
sudo apt install python3-pip (If you don't have python)
pip3 install django
```

Then create database: 
```
python manage.py makemigrations
python manage.py migrate
```

Then create a superuser to manage the admin backend:
```
python manage.py createsuperuser
python manage.py runserver
```

Visit ```http://127.0.0.1:8000/accounts/signup``` to register

Visit ```http://127.0.0.1:8000/accounts/login``` to login

Visit ```http://127.0.0.1:8000/admin``` to login the Django Admin Backend
