Django is free & open source web framework to develop web applications...It follows `MVT(Model(ORM), View(logic),Template)` architecture. Django is maintained by Django Software foundation (DSF).

Django is released in 2003 as an internal project at lowrence journal-World newspaper..Creator is **Adrian Holovaty, Simon Willison**...After testing this framework with high traffic its released _21st July, 2005_ as open source project.

Django name is based on famous guitarist **Django Reinhardt**

Top 5 features of Django:-

- Fast(95% of work can be done by Django)
- Fully loaded(Battery included)
- Security
- Scalability(handle high traffic)
- Versatile(small projects to large projects)

Django project is collection of applications & configuration info

type `django-admin startproject firstProject` for creating project.

folder tree

```
firstProject
	manage.py
	firstProject
		__init__.py
		settings.py
		wsgi.py(web server gateway interface)
		asgi.py
		urls.py
```

type `python manage.py startapp firstApp` for creating App

folder tree

```
firstApp
	__init__.py
	models.py
	admin.py
	tests.py
	views.py
	apps.py
	migrations
		__init__.py
```

to run the server type `python manage.py runserver`. default server is `127.0.0.1:8000` but we can chage the port also by typing `python mange.py runserver 7777`

**Steps to develop Django Projects**

- Create Project
- Create Application
- Installed app in settings.py
- Create views.py file to provide response
  - Every view function takes _req_ as an input & return _response_ as output
- For every view function we've to provide a separate urlpattern inside urls.py
  - by using this url user can send a req
- Run server
- Send a req to the server

**How server response a req**

- first server will get request
- server opens urls.py file
- server identifies the corresponding view function from urls.py
- server will execute corresponding view function & provide response to the user

**MVC Pattern**

- M - Model(Business logic)
- V - views(Presentation)
- C - Controller(Co-ordination)

**MVT Pattern**

- M - Model(database logic)
- V - views(request handler)
- T - template(Presentation)
- Co-ordination is take care django itself

**URLs:** While it is possible to process requests from every single URL via a single function, it is much more maintainable to write a separate view function to handle each resource. A URL mapper is used to redirect HTTP requests to the appropriate view based on the request URL. The URL mapper can also match particular patterns of strings or digits that appear in a URL, and pass these to a view function as data.

**View:** A view is a request handler function, which receives HTTP requests and returns HTTP responses. Views access the data needed to satisfy requests via models, and also delegate the formatting of the response to templates.

**Models:** Models are Python objects that define the structure of an application’s data and provide mechanisms to manage (add, modify, delete) and query records in the database.

**Templates:** A template is a text file defining the structure or layout of a file (such as an HTML page), with placeholders used to represent actual content. A view can dynamically create an HTML page using an HTML template, populating it with data from a model. A template can be used to define the structure of any type of file; it doesn’t have to be HTML.

```py
# Join directory (django follows abs path)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
```

**steps to develop template based application**

- Create Project
- Create Application
- Installed app in settings.py
- Create `templates` folder in main project folder(where manage.py file stay).
  - In that templates folder we've to create subfolders according to app names, these subfolders will contain app related files.
- Add `templates` folder to setting.py file so that django can aware.
  - `TEMPLATE_DIR=os.path.join(BASE_DIR, 'templates')` `django 2.x`
- Create template html file with our required response
- Create view functions in views.py file
- Create url pattern either projectURL or appURL
- Run Server
- Send a request to server

**insert static files**

- Inside main project folder create a folder 'static'
  - inside static create subfolders for images, css, js
  - `STATIC_DIR = os.path.join(BASE_DIR, 'static')` `django 2.x`
  - add this at the bottom of setting.py file `STATICFILES_DIRS = [STATIC_DIR]`
- all procedure same as previously written
- insert `{% load static %}` at the front of html file to make all static files available in html file
- include css files
  - `<link rel="stylesheet" href="{% static 'css/demo.css' %}"`
  - if it is external css `<link rel="stylesheet" href="">`
  - separate css for each file
    - {% block css %} {% enblock %} `base.html`
    - {% block css %} <link rel='' href=''> {% enblock %} `others.html`
- `{{ variable }}` template variable
- `{% tag %}` template tag
- include image files
  - `<img src="{% static 'images/sunny.jpg' %}" alt="">`
  - if it is external url `<img src="" alt="">`
- include anchor tag
  - `<a href="{% url '...' %}">text</a>` | `<a href=/pageName target=''>...</a>`
  - if it is external url `<a href=''>...</a>`
- title
  - base.html - `<title>{% block title %}{% endblock %}</title>`
  - rest of files - `{% block title %} {{ var }} {% endblock %}`

**Dynamic & Static route**

```py
# urls.py
purlpatterns = [
    path('', views.index, name='index'), # Static
    path('<int:age>/', views.show_age, name='show_age'), # dynamic
    # route name must be matched with views parameter 'age'
]

# views.py
def index(request):
	return HttpResponse('<h1>Hello World</h1>')

def show_age(request, age):
	return HttpResponse(f'<h2>I am {age} years old</h2>')

https://localhost:8000/25 (25 passed to the view as a string)
```

**Path converters**

**str** - Matches any non-empty string, excluding the path separator, `/`.

**int** - Matches zero or any positive integer.

**slug** - Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters. For example, `building-your-1st-django-site`.

**uuid** - Matches a formatted UUID.

**path** - Matches any non-empty string, including the path separator, `/`. This allows us to match against a complete URL path rather than a segment of a URL path, as with `str`.

**Check database connection is ok or no**

```py
>>> from django.db import connection
>>> connection.cursor()

# if it doesn't return object, then there might be a problem in db connection
```

**MySQL Connection**

```py
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'NameOfTheDatabase',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': 'localhost',
		'PORT': 3306,
	}
}
```

**models.py**

`python manage.py makemigrations` -> convert model classes into sql code

`python manage.py migrate` -> execute sql query to create database table

`id` is provided by django itself. sql table name will be something like this -> `appName_modelClass`(lowercase)

**How to see tables in sqlit3**

to see generated sql code `python manage.py sqlmigrate AppName MigratefileName`

to see the sql table -> run `python manage.py dbshell`, it will open sqlite shell, then type `.tables`. It will show all the available tables in sqlit3. then type

```
.header on
.mode column
pragma table_info("NameOf the Table");
```

**admin interface**

first we've to import model classes in admin.py.. then register `admin.site.register(NameOfTheModelClass)`

**fetch data from database into views.py**

write `emp_name = Employee.objects.all()`

**Process to generate django forms**

```py
# forms.py
from django import forms

class StudentRegistation(forms.Form):
	name = forms.CharField(label='NAME', widget=forms.TextInput(attrs={'class': 'form-field'}))
	marks = forms.IntegerField()

# views.py
from . import forms
form = forms.StudentRegistation()
return render(request, '', context={'form': form})
```

**How to grab input data from html to views.py**

```py
# get request
feedback = forms.FeedBackForm()

## Post request
if request.method == 'POST':
	feedback = forms.FeedBackForm(request.POST)
	if feedback.is_valid():
		# there is one dict `cleaned_data` who captures all forms variable
		print(f'Name {feedback.cleaned_data['name']}') # must be matched with forms varName

return render(request, 'formApp/feedback.html', contenxt = {'feedback': feedback})
```

**Many to one Relationship**

- _models.foreignkey_ is many to one relationship. Employee & Company
  - `models.CASCADE` means that if an object of the company is deleted, then the employees associated with that company are also deleted

```py
from django.db import models
from datetime import date
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=264,unique=True)
    number_of_employees= models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Employee(models.Model):

    employee_name = models.CharField(max_length=264, unique= True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default= date.today)

    def __str__(self):
        return self.employee_name
```

**Many to Many Relationship**

- `models.ManyToManyField` is used for many to many relationship
  - one project can have multiple employees, and one employee can work on multiple projects

```py
from django.db import models
from datetime import date
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=264,unique=True)
    number_of_employees= models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Employee(models.Model):

    employee_name = models.CharField(max_length=264, unique= True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default= date.today)

    def __str__(self):
        return self.employee_name

class Project(models.Model):

    project_name = models.CharField(max_length=264, unique= True)
    employee_name = models.ManyToManyField('Employee')

    def __str__(self):
        return self.project_name
```

**one to one relationship**

`models.OnetoOneFiled` is one project will have only one employee as a Team Lead. - one employee will be the Team Lead for only one project.

```py
from django.db import models
from datetime import date
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=264,unique=True)
    number_of_employees= models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Employee(models.Model):

    employee_name = models.CharField(max_length=264, unique= True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default= date.today)

    def __str__(self):
        return self.employee_name

class Project(models.Model):

    project_name = models.CharField(max_length=264, unique= True)
    employee_name = models.ManyToManyField('Employee')
    team_lead = models.OneToOneField('Employee', on_delete=models.CASCADE, related_name='team_lead')

    def __str__(self):
        return self.project_name
```

Widgets should not be confused with fields, as fields represent the input validation logic, whereas widgets represent the HTML rendering of the fields.

**http request methods**

- GET (read operation) ->
  - open browser & type url and submit
  - any hyperlink
  - default `<form action=''></form>` is get method
- POST (update operation) ->
  - without `<form action='' method='POST'>`, not possible to send post request
    - submit/login account
- MOVE
- DELETE
- CONNECT
- TRACE
- PUT
- HEAD
- LOCK
- PROFIND
- OPTIONS

**Django forms validation**

- Explicit - custom validation method name must start with `clean_attributName` which gonna validate
- Implicit - do it django by itself
- we can also write our own validation function
  - after write function set that inside attribute `name=forms.CharField(validators=[functionName])`
- `from django.core import validators` built in validator
  - `name=forms.CharField(validators=[validators.maxlengthvalidator(40)])`
- we can also write all custom validation into single function
- `def clean(self): cleaned_data = super().clean()`

How to save User

```py
from django.contrib.auth.models import User
from django.db import IntegrityError

def home(req):
		try:
		    user = User.object.create_user(username='', email='', password='', first_name='', last_name='')
		    user.save()
		except IntegrityError as e:
				print(e)

return HttpResponse('')
```

**How to Performs form validation**

- by using `clean_filename()` ❌ (not recommended)
- by using inbuilt validators `from django.core import validators`
- by using validations by using same validators variable
- by using a single `clean()` method ❌ (not recommended)

**How to save forms values in database**

```py
if request.method == 'POST':
        reg = forms.RegistrationFormModel(request.POST)
        if reg.is_valid():
            reg.save(commit=True) # this will save data inside database
```

**Advanced templates**

- Template Inheritance
- Template tag filters

**How to define custom filters**

- override default filter's functionality also possible
- make a `templatetags[name is fixed]` folder inside `app`
- inside folder create `__init__.py`
- create custom filter file `anyName.py`
- then

```py
# this 2 lines are fixed
from django import template
register = template.Library()

@register.filter(name='swapcase') # we can also use this decorator's style also
def swap(string):
  return string.swapcase()

register.filter(name='swapcase', filter_func=swap)
```

- Inside template file load this filter `{% load swap %}`[swap is file name]

**Session Management**

- some methods/process required at server side to remember previous request that is called session
- [Session vs. Cookies | Difference between Session and Cookies](https://www.javatpoint.com/session-vs-cookies)

_Session management methods_

- cookies
- django session framework (Session API)
- hidden form fields
- url rewriting

_Session management by using cookies_

```py
# adding this cookie to the response object
response.set_cookie(cookiename, cookievalue)

# when 2nd req coming from same person, it will check cookies
# get cookies object
request.COOKIE.get(cookiename, 'no cookie is present)
```

Sample_Example

```py
def count_view(request):
  count = int(request.COOKIES.get('count', 0))
  new_count = count + 1
  response = render(request, 'found.html', {'count': new_count})
  response.set_cookie('count', new_count)
  return response
```

There are 2 types of cookies available

- Temporary
  - If we aren't setting any `max_age=NumberOfSec` for the cookies as long as browser is open cookies stay. If we close browser the cookies will gone...
- Permanent/Persistent
  - If we set `max_age=NumberOfSec` for the cookies then it will not vanish until the time is come. It will stay in client't machine.

```py
response.set_cookie(cookieName, cookieValue, max_age=180) # persistent
response.set_cookie(cookieName, cookieValue) # Temporary
```

_Limitations of Cookies_

- by using cookies we can store only _4KB_ information
- less security
- cookie information is always string type
- every time browser has to send all cookies related to that application request. Network traffic will be raised.
- Max number of cookies supported by browser is always fixed

> **Django Session Framework**

when client sent a request to the server, server creates a object which is called `sessionId`. This is store all related information about client. By default Django session keeps data in 2 weeks. SessionId's information is encrypted only server can decrypt it.

```py
# COOKIE
# set data
response.set_cookie(cookieName, cookieValue, max_age=None)
# get data
request.COOKIES.get(cookieName, '')

# SESSION
# set data
request.session['name']=value

# get data
request.session.get('count', 0)

# set expiry date
request.session.set_expiry(seconds)
```

---

_Important methods related to session_

- `request.session.set_expiry(0)` session will expire once we close the browser
- if we are not performing any operation on the session specified amount of time(max inactive interval) then session will br expired automatically.
- But in the case of COOKIES after max time passed cookies will be gone...
- if you wanna delete session keys, you have to first set `SESSION_SAVE_EVERY_REQUEST=True` in `settings.py`.

```py
def home_view(request):
  count = request.session.get('count', 0)
  new_count = count + 1
  request.session['count'] = new_count
  print(request.session.get_expiry_age())
  print(request.session.get_expiry_date())
  return render(request, 'page-count.html', {'count': new_count})
```

> Before run `python manage.py runserver` run first `python manage.py migrate` because session’s data saves in database

> **Python Database Connectivity**

In python if you want to communicate with database some driver is required.

_for Oracle→_

`pip install cx_Oracle`

_for mySQL→_

`pip install pymysql`

**Steps to connect database with python**

- import database specific module
- establish connection between python & database

  ```python
  # for Oracle
  con = cx_Oracle('user/password@localhost')

  # for mySQL
  con = pymysql(host='localhost', database='databaseName', user='userName', password='Password')
  ```

- For send SQL queries & fetch the result cursor object is required
  ```python
  cursor = con.cursor()
  ```
- Execute SQL
  ```python
  cursor.execute('sqlQuery')
  cursor.executescript('sqlQueries') # string of sql queries separated by ;
  cursor.executemany() # parameterized sql queries
  ```
- Fetch the result
  ```python
  cursor.fetchone() # only one query return
  cursor.fetchall() # return all queries as list of tuples [(),]
  cursor.fetchmany(n) # n number of queries
  ```
- If we modify any data then after modification
  - DDL → create, drop & alter
  - DML → insert, delete and update

we’ve to commit `commit()`. This only for DML. Without commit modify won’t be reflected

- close the connection
  ```python
  cursor.close()
  con.close()
  ```

**User Authentication**

Auth module take care login, logout. it requires one table: user

restrict to access the page before login

```py
from django.contrib.auth.decorators import login_required

# use this decorator which page you wanna restrict
@login_required
def java_page(request):
  ....
```

after set this up, when you click the link it will show login page, if you don't config your url it will throw error
and expect `localhost:8000/accounts/login` this url. so we've to set it.

```py
path('accounts/', include('django.contrib.auth.urls'))`,
```

then it expects template at `registration/login.html`

add `LOGIN_REDIRECT_URL = '/'` this in `settings.py`

LOGOUT_REDIRECT_URL = '/logout'

```py
def signupForm_view(request):
    signup_form = forms.SignUpForm()
    if request.method == 'POST':
        signup_form = forms.SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'signup.html', {'signup': signup_form})
```

### Class Based view

`from django.views import generice`



__Generic view__

- View
    ```py
    class HelloView(generic.View):
        def get(self, request): # for get request
            return HttpResponse('<h1></h1>')
    ```
- TemplateView
    ```py
    class HelloTemplateView(generic.TemplateView):
        template_name = 'x.html'
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context[key] = value 
            return context
    ```

**Model Related views**

- ListView - list all records
    ```py
    class BooksListView(generic.ListView):
    model = models.Book
    # default template_name - AppName/modelName_list.html
    # default_context object - modelName_list

    # === we can override ===
    # template_name = 'book_list.html'
    # context_object_name = 'books'
    ```
- DetailView - get details of a particular record
    ```py
    class BookDetailView(generic.DetailView):
        model = models.Book

        # === default ===
        # template_name - testApp/book_detail.html
        # context object - book or object

    # urls.py
    path('details/<int:pk>/', viwes.BookDetailView.as_view())
    ```
- CreateView - create record
- DeleteView - delete record
- UpdateView - update record
