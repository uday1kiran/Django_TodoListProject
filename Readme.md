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

python3 manage.py makemigrations #to create migrations for new model data,once done you can run migrate command


reference project: https://github.com/zappycode/django3-todowoo-project

