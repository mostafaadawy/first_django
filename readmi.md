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
- in product model to save data  we discripbe the required data fields
- adding our in in settings
- as we change something in database we have to call makemigration to allow checking models and adding its effect in database `python manage.py makemigrations`
- do not make `python manage.py migrate`  after every time we make `python manage.py makemigrations`
- when asking for Quit, and let me add a default in models.py we select this option and adding default to the field that we just want to insert but the question is what is this about?
- actually when you create a table in database it doesn't matter what is default except for some cases but the most required default value will be when editing a table , here the database wants to know how to deal with previous records where it is live table that mean it may contain records
- so to solve this issue we have to defined a default value for the newly added field such as `summary = models.TextField(default="this is default example")`
- run the 2 command makemigrations and migrate again
- we have to register model in products admin.py to use it such as `from .models import Product` where `.` in `.model` is called relative import it means in the same folder 
- then we have to register it like `admin.site.register(Product)` when we registering it in admin it will add it in view and edite save and update all crude operations will be made automatically  and we can check this in browser admin

## Create App Objects in python shell like laravel tinker
- as we using admin before to create product know we will use python shell
- we can access python shell by cmd `python manage.py shell`
- the difference from python is that shell work as wrapper connects our project so when we import or call some apps component in shell it is work it is something like laravel tinker
- so we can write the same code as we write it in admin in product to test it line by line or to implement something
- this code snippets we can write in shell
```sh
>> from products.models import Product
>>> from products.models import Product
>>> Product.objects.all()
<QuerySet [<Product: Product object (1)>]>
>>> Product.objects.create(title='Prooduct 2', description='from shell', price='200', summary='hey summary shell')
<Product: Product object (2)>
>>> 
```
- where `Product.objects.all() will call all records from Products table
- and also we can create new object/record
## New Model Fields 
- previous example shows the textfield but actually we have many field types
- Note if we need to cancel all migrations in this project we can delete all files in product migrations and pycache leave init only
- we can also delete db.sqlite3 database
- from django modelfields we can try these fields
- if we use charField max_length is required as same as decimalField requires decimal place and max digits you can check the documentation of django and also when error the interpreter will tell us
- we can remove default from summary where it is now create at the beginning
- make the 2 migration commands makemigrations and migrate
- as we already deling our sqlite file so our superuser is deleted so we need to create superuser with same credentials  