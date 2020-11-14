created project using:

django-admin startproject todowoo

created app inside it using:
python3 manage.py startapp todo

registered app to the main settings.py:
todowoo\todowoo\settings.py
INSTALLED_APPS = [
    .......
	'todo',
]


...... represents other data exists prviously

to migrate previous code in installed_apps like auth,etc:
python3 manage.py migrate

to get admin user to access admin page.
python3 manage.py createsuperuser
