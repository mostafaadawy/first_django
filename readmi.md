# Django based video tutorial in this [link](https://www.youtube.com/watch?v=F5mRW0jo-U4)
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
- adding our apps in settings
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
- we have to wrap our view code to a route to access it
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
# Django Templating Engine Basics
- here we will define how to shrink the render html to layout extended and just we add the deferent code area 
- getting variable data by calling through `{{  }}` inside the html file
- to create base layout create file html base,html
- inside this file we add all required scripts styles title and meta data 
- inside body prepare the place where to insert different code by `{% block content %}{% endblock %}`
- in other files we call the base file `{% extends 'base.html'%}`
- wrap thw required file code by 
```sh
{% block content %}
        <!-- replace me -->
 {% endblock %}
```
- at this point we have make block inheritance 
- now if we make navbar in base it will appear in all and so on
- we can make in base file many blocks with deffent names and in files we select whick block we need to change  for example
```sh
{% block content2 %}
        <!-- replace me -->
 {% endblock %}
```
# include template Tag 
- the objective of inheritance to remove redundant code and to reduce complexly and to allow more reduction we can use `{% include 'navbar.html'%}` in base file or even others and that defers from previous where it will insert that code patch to your template as it is and that instead of writing in one file a lot of code that makes you confused

# Contexting passing data Rendering Context in Template
- collapsing our varaiables that we want to send in my_context object
- using `{{ }}` to extract data in html
- using `{% %}` to call python commands inside html
- example for loop and if 
```sh
<ul>
    {% for item in My_List %}
            {% if item == 111 %}
                    <li>
                            {{ forloop.counter }}- {{ item }} is integer
                    </li>
            {% elif item == "111" %}
                    <li>
                            {{ forloop.counter }}- {{ item }} is string
                    </li>
            {% else %}
                    <li>
                            {{ forloop.counter }}- {{ item }} is boolean
                    </li>
            {% endif %}
    {% endfor %}
</ul>
```
- where we send the list from view.py
```sh
def about_view(request, *args, **kwargs):
    my_context = {
        "My_text": "Context Text",
        "My_number": 123456789,
        "My_List": [111, "111", True]
    }
    return render(request, "about.html", my_context)
```
- here is the extra feature from python `{{ forloop.counter }}` returns the index of the current element in the loop

# Builtin tag filter
- it is a fast function that can be used 
- example of addition number to item `{{ item|add:100 }}`
- example of make first char capital `{{ My_text|capfirst }}`
- we can stack many filter together ` <h1>{{ My_text|capfirst|upper|add:" hi" }}</h1>`  
- for more filters such as cycle and filters check the [doc](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/)
- other useful filters `safe` or `striptags` that extract html and render it but securely unsafe and `title` that titles certain data

# Render Data from Database with a Model
- try dealing with model from shell first `python manage.py shell`
- as we can see we can retrive data from database as follows where dir method is used to display properties or methods comes from database table or model 
```sh
>>> from products.models import Product
>>> obj = Product.objects.get(id=1)
>>> dir(obj)
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'check', 'checkThat', 'clean', 'clean_fields', 'date_error_message', 'delete', 'description', 'from_db', 'full_clean', 'get_deferred_fields', 'id', 'objects', 'pk', 'prepare_database_save', 'price', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'summary', 'title', 'unique_error_message', 'validate_unique']
>>> obj.title
'first product'
>>>
```
# at that moment we were trying to test but the right thing is to keep all related methods in one place so we will work in product view
- create folder product in template to contain all rendered files related to product
- in product view.py create function to return render file contexted with product get to show detail view
- add url to link view/controller and url
- can double check condition `{% if description != None and description != "" %} ` 
- an error that must not happen we have to take care because of lake of interpreter where  i forgot space after != and "" and that caused error

- instead of sending individuals from object we can send object itself

# How Django Templates Load with Apps
- when we call render for a file we override a template code in the django that can be shown when no path found
```sh
django.template.loaders.app_directories.Loader: C:\Users\Dell\AppData\Local\Programs\Python\Python37\lib\site-packages\django\contrib\admin\templates\product\product_detail.html (Source does not exist)
django.template.loaders.app_directories.Loader: C:\Users\Dell\AppData\Local\Programs\Python\Python37\lib\site-packages\django\contrib\auth\templates\product\product_detail.html (Source does not exist)
```
# Django Model Forms
- Form in django is used to apply validation and pending model in view create and other crude operations 
- we can begin using form by  create file forms.py
- here is a code snippet 
```sh
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
```
- before going deeply in code structure we have to know that form and other standards from the framework make a lot of stuff easy but standard so we can accept the standard code and in this case we can easily implement our issue while django or framework's allow to custom every code piece according to oue objective
- as we explain before we can use forms to draw our views and make our validations and save our model data in one or two line of codes 
- from previous code snippet we can notice that we have to import django forms to use it and import the model to bend it with the form also in the meta data we have to bend the required fields as same bending model itself

# Raw HTML Form
- we make another template product_test for testing raw html for form
- note that form by default if we do not define the method is get method
- CSRF Is security must fro POST methods
- we can use form actions for liking a route where `.` period means same url used currently 
- `action ="https://www.google.com/search" and method "GET" must be get  rename the search ` and `input name `to `q` so you can search google
- `action="."` return to same url
- taking care of method type

# Pure Django Form
- we create class RawProductForm in forms to test
- it extends or use `class RawProductForm(forms.Form):` `form.Forms` not `ModelForm` as in `class ProductForm(forms.ModelForm):` it is not bended  to model so no meta
- in the first case `bending model ` it inherits the data type of fields from the model but in the second case standard form it should contains definitions for every field datatype
- the fields datatype can be defined form.name where these data type are very close to model.name data types with a very small differences such as we may use form.CharField instead of model.textfield in model
- check django model data fields and forms data fields 
- when we call the form in view.py `my_from = RawProductForm(request.POST)` it will do validations in this class which is until now just required fields
- while calling `my_from = RawProductForm()` with empty arguments to use in view drawing and it matches ``my_from = RawProductForm(equest.GET)` but .GET doesn't contain anything so keep it empty
- as our from is not bended so we cant use `form.save()` but we have to save it using `Product.objects.create(my_from.cleaned_data)`
- the cleaned data is different data type than excepted to create so it gives this error
```sh
TypeError at /create/
create() takes 1 positional argument but 2 were given
```
- the solution is to use `**` to spread arguments inside create `Product.objects.create(**my_from.cleaned_data)`
# important Note: the differences between first form model is that it bends with model it save make crude operations and also validates data while raw html is describing how to create raw inputs in form in html but the recent pure django form explains only validation not bended form


# Form Widgets
- every field setting for validate and view
- default for form core as django documentation  required true is default so in each field argument we set the different required argument such as if not required `required=False`
- we can draw label to input just by writing it as argument in field in form
- here we have the ability to change widget or view  and also custom validation
- code snippets
```sh
description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "placeholder": "HI Janna",
            "class": "new-class-name two",
            "id": "desc",
            "rows": 12,
            "cols": 120,

        }
    ))
```
# Form Validation Methods
- there are a lot of validation fields and methods
- when we custom we override the default
- return to commented first form method the standard one 
- check that code snippet 
```sh
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
```
- we can custom the widget and by overriding it such as 

```sh
class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Title custom', widget=forms.TextInput(
        attrs={
            "placeholder": "HI Janna",
        }
    ))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "placeholder": "HI Janna",
            "class": "new-class-name two",
            "id": "desc",
            "rows": 12,
            "cols": 120,

        }
    ))
    price = forms.DecimalField(initial=155.5)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
```
- to make validation we create function `def clean_fieldName(self, *args, **kwargs):` for example  `def clean_title(self, *args, **kwargs):`
- so as the output data after validation can be called by cleaned data we have to prefix the filed by clean
- it is recommended to use the default validations first as follows `title= self.cleaned_data.get("title")`
- then adding some other custom conditions check code snippets
```sh
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "mos" in title:
            raise forms.ValidationError("this is not contains mos")
        if len(title) < 4:
            raise forms.ValidationError("short")
        return title
```
- we can check email just by form field type `email = forms.EmailField()`

# Initial values for Forms
- that is used in edit forms so we can initilize the iputs and also we can get  an instance of the object whichh in our caase is record or show check the snippet
```sh
def render_initial_data(request):
    initial_data = {
        'title': 'this is initial data title',
    }
    obj = Product.objects.get(id=1)
    my_form = ProductForm(request.POST or None,
                          initial=initial_data, instance=obj)
    if my_form.is_valid():
        my_form.save()
        my_form = ProductForm()

    context = {'form': my_form}
    return render(request, "products/product_create.html", context)
```
- in this snippet  initial=initial_data will overrides instance=obj
- do not forget to add url to that function

# Dynamic URL Routing
- it means that it contains variables in the url such as what we need for show() edit() in crude operation
- in url link we add that variable as follows: `path('dynamic/<int:my_id>/', dynamic_lookup_view, name="dynamic_lookup_view"),`
- where id is sent here `<int:my_id>`
- and received here in the function `def dynamic_lookup_view(request, my_id):` same name
- then we use it to get the right object or record `obj = Product.objects.get(id=my_id)`
- so this obj can be send to the context 
- note that `<int:my_id>` we can define deferent data types that int like string slug or others
# Handle Missing Objects
- it discusses what to do if requiring object id that is not exist no record
- to handel missing object we use get_object_or_404 class from django `from django.shortcuts import render, get_object_or_404` in the controller or view.py
- we call the object using that function and that will not return uncontrolled error as before but returning a vialed error 404 
- using `obj = get_object_or_404(Product, id=my_id)` instead of `obj = Product.objects.get(id=my_id)`
- another way is to use `from django.http import Http404` instead of  `from django.shortcuts import render, get_object_or_404`
- then using try except like try catch as follows:
```sh
try:
        obj = Product.objects.get(id=my_id)
    except:
        raise Http404
```
- so here we handled that exception 
# Delete and Confirm
- delete is justed executed by `obj.delete()` and can be handled from get method but for insuring that he mean the delete we make it in POST that mean we need to submit a form
- in the delete we check first if it is post it means that the submission is done through yes submit in the delete form
- calling delete then calling redirect to return to view check the snippets 
- controllers 
```sh
def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.POST:
        # confirming delete
        obj.delete()
        print('debug', obj)
        return redirect('/products/')
        # return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context)
```
- url code
```sh
   path('products/<int:my_id>/delete/',
         product_delete_view, name="product_delete"),
```
- code html
```sh
{% extends 'base.html'%}

{% block content %}
<form action="." method="POST"> 
    {% csrf_token %}
    <h1>Do you want to delete the product "{{ object.title }}"?</h1>
    <p>
        <a href="../">Cancel</a>
    </p>
    <input type="submit" value="Yes">
</form>
{% endblock %}
```
# View of a List of Database Objects
- match index in laravel
- create url ` path('product_list/', product_list_view, name='list'),`
- create `queryset = Product.objects.all()` to call all and send the list to be shown in list

# Dynamic Linking of URLs
- using href and a to link a url
- we do it in a normal a ref but if want to change url it becomes so difficult so use instance method in the model that is used this method keeps a reference for all used urls so we can change any time 
- in model.py in product 
```sh
def get_absolute_url(self):
    return f"/product/{self.id}/"
```
- `f` is used to stringify the number
- so we can use in html a ref as follows: `<a href="{{ item.get_absolute_url  }}">` instead of `<a href="/product/{{ item.id }}">`

# Django URLs Reverse
- we will use reserved function called `reverse` that takes reads the keywords `kwargs` from the link which is id in the url and use it in get_absolute_url 
- to use `reverse` we have to import `from django.urls import reverse`
- `return f"/product/{self.id}/"` become `return reverse("dynamic_lookup_view", kwargs={"id": self.id})`
- where `dynamic_lookup_view` is the name of url ` path('product/<int:my_id>/', dynamic_lookup_view, name="dynamic_lookup_view"),`
- here if url is changed dynamically will be updated as long as the link name is used in reverse function

# App URLs and NameSpacing 
- using reverse function allow us to change and make it dynamic where it is based name but how about if same name is used?
- it will redirect to wrong urls
- to avoid this wrong direction abd to make it modular in order to all folder app and just concatenating to our project and to simplify the url file we can use app url and namesapacing as follows
- first create url file inside our module or component or app cut and past its related links from the main url file and past it in url inside app product
- in main url include the sub url class of the product 
- if we use the links we have to take care that we have to increase in browser link prefix name for the product so we have to avoid duplication in links we past to sub url or app url file
- we can use namespace to prevent wrong redirection where we can include it when calling a path that define which namespasce we belong
- do not forget to modify the reverse model get url function to have the namespace as follows
```sh
def get_absolute_url(self):
        return reverse("products:dynamic_lookup_view", kwargs={"id": self.id})
```
- adding some important links and commenting others
- adding some redirects
- creating href from list and navbar
# Class Based View List View
- Create a new App named blog `python manage.py startapp blog`
- Add blog to your django project `in settings.py add blog to installed apps`
- Create a Model named article `in models.py create class input argument models.Model and add fields to it `
- run Migration `python manage.py make migrations` and `python manage.py make migrate`
- Create a Model Form for article create forms.py and import forms from django and article model from models can check product forms for view and validations 
- Create `article_list.html` and `article_detail.html` Template in folder blog
- Add article Model to the admin in blog in admin.py register the new model for this app `admin.site.register(Article)` so it can be shown and crude operated from admin automatically
- Save a new article object in the admin from ui browser
- confuse? start [here](https://kirr.co/9ypik6)
- create url for Articles 

# Class Based Views Detail view
- note pk is id same name
- the idea is instead of using functions methods using or based class in other word bending the class to the crude that so to execute such methodology we use kwargs to extract the id or other url parameters 
- benefit of bending class is that we can access its properties from the view
- we use the based class method where it is the easiest brief way to implement
- we used it as class to inherit other ready existing classes such as `CreateView, DetailView, ListView, UpdateView, DeleteView` by importing them from `django.views.generic ` and we use `.as_view()` to convert the class to view method actually we call view method from this class 
- these classes work in systematic manner it allow rendering dealing with model anf forms and validation in one step
- it searches for html templates in same path as the name and for files underscored with list detail as classes names
- check this code snippet
```sh
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html
```
- class ArticleListView inherits from ListView and we have to assign variable template_name which is class property and we override it by the path
- the name of html file must ends with _list as we inherits from ListView
- queryset also in list must be assigned to the model get data where it linked directly to context `object_list`as we use the name `queryset`
- so how to call class in url link which needs view method , but this issue is solved just `.as_view()` which calls view function `path('', ArticleListView.as_view(), name='article-list'),` 
- for class details same as list in naming conventions we use in the tail `_detail ` in html and use as view function in url
- and to get object in html we restricted by assigning data to `queryset` but as detail is assigned for one id as show crude we hve to define function get_object that reads `kwargs` id then we return `ModelName.objects.get(id=id) or get_oject_or_404(ModelName, id=id) check the code snippet 
```sh
class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
```
- as we can see from the code we can neglect queryset where we already get object by get_object function
### create method based class
- do the same as list do the required naming and assignments for `queryset` and html file name `_create` and and url use `.as_view()`
- also there is a required assignment is to assign the `form_class= ModelForm` for validation
- we also have functions that we can use in the classes such as form_vail to check validity and we can use it also in debugging and this function is done by default in our model
- we can also define where to go after success in `success_url`
- check the code snippet

```sh
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #    return '/'

```
- in model we can create function `get_absolute_url()` that uses the kwargs in reverse function to return the url from the url name and id 
- this function can be called as any property and we can use it with detail and update i.e. any functions in crude that uses id
- all the methods or properties in these based classes is exists with default and we have to override it or assign value to it or use it 
- update method or class is same as create except we need and object from the object we want to edit or update so the only thing that is increaesd on the previous code is adding `get_object` as in detail and other functions as detail check the code snippet
```sh
class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
```
### for delete view
- for delete the same restrictions with naming conversions  with using function that is defined the object and delete it self is self defined from delete class we extended check the code snippet
```sh
class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')
```
- as we delete the object if return it will give error where no record for that id in the database so we have to define the get_success to route for another link
- as modular project all belongs to app blog should be inside even templates
- <p style="color:red"> do not forget to make update or edit link GET method to get required object where POST is assigned to send not get </p>

### Function Based View to class Based View
- this is the third method that we can use the set and get for view as class 
- first of all we will create new app called course so we will do the same previous steps
- Create a new App named courses `python manage.py startapp courses`
- Add course to your django project `in settings.py add courses to installed apps`
- Create a Model named course `in models.py create class input argument models.Model and add fields to it `
- run Migration `python manage.py makemigrations` and `python manage.py migrate`
- Create a Model Form for article create forms.py and import forms from django and article model from models can check product forms for view and validations 
- Create `course_list.html` and `course_detail.html`and `course_create.html` and `course_delete.html` and `course_update.html` Template in folder courses templates
- Add article Model to the admin in courses in admin.py register the new model for this app `admin.site.register(Course)` so it can be shown and crude operated from admin automatically
- Save a new course object in the admin from ui browser
- confuse? start [here](https://kirr.co/9ypik6)
- create url for Courses 
- do not forget to include urls file links in main url in the project
- list view in class based note that function in view function based name is do not matter but in class the name is really matter we should restricted by naming convictions so we can use `my_fbv` function inside class `CourseView` but rename it to get where we will deal with it in class as `set/post and get`
- we get an error if we use `def get(request, *args, **kwargs):` where as class we have to include self where it is class and without self we miss meta data `'CourseView' object has no attribute 'META'`
- to solve this issue insert self in the call to get the meta data from the class `def get(self,request, *args, **kwargs):`

