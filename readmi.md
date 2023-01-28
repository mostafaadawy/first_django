# Django
## First Project
### Preparing Enviroment
python django depends on working through wrapper or virtual environment. so the first begins if our operating system is windows is to use git bach terminal and install python and pip if not installed
### we can check installed python version by this cmd
```sh
python --version
python3 --version
```
- make folder to contain the virtual system at all `mkdir django_the_first_project` and inside the folder `cd django_the_first_project/`
- install pip if not installed then install virtualenv `pip install virtualenv` to install virtual machine creator.
- create virtual machine instance to contain in an isolated environment the required prerequisite `virtualenv -p python .` where  `period .` means to name the virtual environment by the same name of it parent folder or project name we can defined the based python that we need and the virtualenv name.
- set our virtual environment active to use it 
```sh
    source ./Scripts/activate
```
- after finishing we can deactivate the environment just deactivate without source deactivate.
```sh
    /Scripts/activate
```
- when it is active only deactivate is just write deactivate
- from the same place install django with the required version as follows:
```sh
   pip install django==2.0.7
```
- to check how is virtualenv isolate we can use `pip freeze` to list the installed packages using pip when virtualenv is activated and when deactivated to find that it is totally separated.
- in case we have many versions of python and we need to use certain one in creating the virtualenv we can use `which python` or python3 to get its path and use it in `virtualenv -p python .` instead of python.
- after installing django we are now ready to create project using the power of command line as `django-admin` if we right it only we  show all commands like php artisan.
- it is recommended to create folder for the project source `mkdir src` and enter it `cd src` but after activating enviroment and installing django with its required version.
- if we need to check the installed package we can check the freeze as follows:
```sh
pip freeze
Django==2.0.7
pytz==2022.7.1
(django_the_first_project)
```
1- now while we are inside the project src folder create the project as follows:
```sh
django-admin startproject first_django
```
- maybe the same name of virualenv no problem

- we can use manage.py which is used for Django commands as next:
```sh
cd first_django
python manage.py runserver
```
- now open the browser by clicking the generated link `127.0.0.1:8000`
# At that moment first_django project repo can be accessed from that [link]()

# start working on the project 
- after `python manage.py runserver` to start the project on browser
- we should migrate database `python manage.py migrate`
- creating superadmin `python manage.py createsuperuser`
- username mostafa login email mostafa_adawy@ymail.com and pw is root123#
- app in django matches component in others
- to create our first app/component 
- not that all whenever we need to make command or use manage.py we have to be the in the root od the project
- creating our first app `python manage.py startapp products`
- creating app blog `python manage.py startapp blog`
- creating app profiles `python manage.py startapp profile`
- creating app cart `python manage.py startapp cart`
-