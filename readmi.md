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
## Change a Model
here is some important notifications about models 
- when we make `makemigartion` at just compare the migrated class fields if the class is already exists or not  to crate it also checking the calling of fields the type and the required argument where it for example refuses to use `charField` without argument `maxLength` 
- in case the class is already exists and there are some new fields to add it must know how to deal with the previous records that does not have that fields in this case the solution is to allow `null = True` or `default= value` or True and that will tell the interpreter how to fell the previous record we can solve this issue in the model file it self before run `migration` or we can do that in the `shell` by selecting the first option and tell him the default value
- so what is the difference between `null= True` , `default =  True` and `blank = False` or `blank =  True` ?
- actually as this is an automatic file generation so model here defines the form validation also so when `blank = False` it means `not required` field and in the edit and view we will notice that the fields name is `normal` while in case it equals `True` the field name by default will be written in `bold` and when trying to summit the form without that field it will pop up a `validation error` of missing field.

the comparison file will be found for each migration in migration folder in the added app/component

# Custom HomePage
- create a new app called pages `python manage.py startapp pages`
- adding app pages to setting Installed Apps
- in pages view.py  it differs from other packages such as laravel or even mvc view here will handel web pages as a controller also
- include HttpResponse to be used  `from django.http import HttpResponse` 
- in function use `def home_view(*args, **kwargs):` where *args specifies the number of non-keyworded arguments that can be passed and the operations that can be performed on the function in Python whereas **kwargs is a variable number of keyworded arguments that can be passed to a function that can perform dictionary operations. using in  packing and unpacking in Python 
## Why do we need *args and **kwargs?

When we are writing Python code, functions are something that we cannot overlook. Functions are beneficial in removing the repetition of code and making it modular . Functions generally need some data to work on, and it can be in the form of strings, numbers, or even other functions. In the programming world, this data is referred to as arguments.

A simple scenario where you will need functions is- Suppose you are running a website to design greeting cards. If you want to display a greeting message like “Hello name_of_user”, you must ask the user to input their name. You will then pass the input to a function that will display the greeting message.

Sometimes it is possible that you can't predict the number of arguments that we will be providing to the function. This can cause the problem, and if you don’t know how to handle it, then you will end up getting stuck writing the same code for variable number of arguments.

*args are **kwargs are the solution of your problem.

### *args in Python [ref](https://www.scaler.com/topics/python/args-and-kwargs-in-python/)

Let us assume that you are building a calculator which only performs multiplication.

You can make a simple function that can do this and that function will look like this-
```sh
def multiply(num1,num2):
    return num1*num2
print("product:", multiply(2,3)) 
```
Output:
```sh
product:6
```
Now you want to multiply three numbers, so you have to make a new function.
```sh
def multiplyThreeNumbers(num1, num2, num3):
    return num1*num2*num3
print("product:",multiplyThreeNumbers(1, 2, 3))
```
Output:
```sh
product:6
```
ou can already see the problem. If you keep going on like this, you will end up doing a lot of functions.

*args can save you the trouble here.

You can use args to solve this problem in a simple and flexible piece of code-
```sh
def multiplyNumbers(*numbers):
    product=1
    for n in numbers:
        product*=n
    return product
print("product:",multiplyNumbers(4,4,4,4,4,4)) 
```
Output:
```sh
product:4096
```
Now that your problem is solved let’s understand what is going on here.

Python has *args, which allows us to pass a variable number of non-keyword arguments to a function. Non-keyword here means that the arguments should not be a dictionary (key-value pair), and they can be numbers or strings.

One thing to note here is that "args" is just an identifier. It can be named anything relevant.

When an asterisk(*) is passed before the variable name in a Python function, then Python understands that here the number of arguments is not fixed. Python makes a tuple of these arguments with the name we use after the asterisk(*) and makes this variable available to us inside the function. This asterisk(*) is called an “unpacking operator”. We will learn more about it further on in the article.

This variable is then available to us inside the function, and we can use it to perform any operation we want. In our case, we iterated (looped) over it and calculated the product of all the numbers.

### **kwargs in Python
*args enable us to pass the variable number of non-keyword arguments to functions, but we cannot use this to pass keyword arguments. Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

**kwargs allows us to pass any number of keyword arguments.

In Python, these keyword arguments are passed to the program as a Python dictionary.

Python will consider any variable name with two asterisks(**) before it as a keyword argument.
```sh
def makeSentence(**words):
    sentence=''
    for word in words.values():
        sentence+=word
    return sentence
 print('Sentence:', makeSentence(a='Kwargs ',b='are ', c='awesome!'))
```
Output:
```sh
Sentence:Kwargs are awesome! 
```
In the makeSentence function, we are iterating over a dictionary, so we have to use values() to use the values. Otherwise, it will only return the keys and not the values.

Another example of how kwargs can be used is given below-
```sh
def whatTechTheyUse(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append("{} uses {}".format(key, value))
    return result
 print(whatTechTheyUse(Google='Angular', Facebook='react', Microsoft='.NET'))
```
Output:
```sh
[‘Google uses Angular’, ‘Facebook uses react’, ‘Microsoft uses .NET’]
```
In this code, we have used .items() because we want to get both the key and the value.

Using Both *args and *kwargs in a Python Function

Now that you have understood args and *kwargs, you might want to design a function that uses both of them. While doing this, the order of the arguments matter, *args has to come before *kwargs.

So if you are using standard arguments along with *args and **kwargs, then you have to follow this order-

Standard Arguments
*args
**kwargs
A simple example of a function that uses standard arguments, *args and **kwargs in Python:
```sh
def printingData(codeName, *args, **kwargs):
    print("I am ", codeName)
    for arg in args:
        print("I am arg: ", arg)
    for keyWord in kwargs.items():
        print("I am kwarg: ", keyWord)
 printingData('007', 'agent', firstName='James', lastName='Bond') 
```
Output:
```sh
  I am 007 
  I am arg: agent 
  I am kwarg: (‘firstName’, ‘James’) 
  I am kwarg: (‘lastname’ , ‘Bond’)
```
### Packing and Unpacking Using *args and **kwargs in Python
The single and double asterisks that we use are called unpacking operators.

Unpacking operators are used to unpack the variables from iterable data types like lists, tuples, and dictionaries.

A single asterisk(*) is used on any iterable given by Python.

The double asterisk(**) is used to iterate over dictionaries.

Let’s take some examples-
```sh
carCompany = ['Audi','BMW','Lamborghini']
print(*carCompany)
```
Output:
```sh
  Audi BMW Lamborghini
```
Here the asterisk(*) passed before carCompany unpacked all the values. In other words, the values are printed as separate strings rather than a list.
```sh
techStackOne = {"React": "Facebook", "Angular" : "Google", "dotNET" : "Microsoft"}
techStackTwo = {"dotNET" : "Microsoft"}
mergedStack = {**techStackOne, **techStackTwo}
print(mergedStack)
```
Output:
```sh
  {'React': 'Facebook', 'Angular': 'Google', 'dotNET': 'Microsoft'}
```
Here the double-asterisk unpacked the key-value pairs inside the mergedStack variable, and thus we get all the key-value pairs in the mergedStack variable. args and kwargs in Python do the same job of unpacking the contained values, but they take different inputs and outputs.
### Conclusion
After learning about *args and **kwargs in Python, you can now successfully utilize their superpowers.

Here are some key points that will help you-
- *args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function
- When using them together, *args should come before **kwargs
- The words “args” and “kwargs” are only a convention, you can use any name of your choice


# View.py 
- we have to wrape our view code to a route to access it
- where in settings we knew that routes in django url file
- in `urls.py` add the route for our app

# URL Routing and requests
- creating some functions for calling httpresponce and import it in urls then create route link for every one 
- to debug reading the received args and kwarg just print it and debug in the console running the server
- `request.user` return the user in debugging we can use with middleware later if logout give `anonymous user` means not logged in

# Django Templating
- where we make our html powerful
- we gonna use some builtin shortcuts template that django has
- ` return render(request, "home.html",{})`  passing the request, file to be rendered and data
- after we creating a folder templates and creating a file html for the render but still we cant not access that file file where templates folder it self is not defined 
- to define the templating folder we have to define the path id dir in setting TEMPLATES as follows `'DIRS': [os.path.join("templates")],`
- do the same for others