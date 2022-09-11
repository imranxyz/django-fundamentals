![Language](https://img.shields.io/badge/Language-Python_3.10-important)&nbsp;
![Django](https://img.shields.io/badge/Framework-Django_2.2-important)&nbsp;
![Update](https://img.shields.io/badge/Last%20Update-September%2009,%202022-brightgreen)&nbsp;
![Completed](https://img.shields.io/badge/Watched_till-53-important)&nbsp;

## Intro to Django

* Django is a free and open source web framework to develop web applications.
* It is written in Python.
* It is based on MVT architecture.
    * MVT - Model View Template
        * Database Logic 
        * Co-ordination is taking care by django itself
    * MVC - Model View Controller
        * Logic Presentation Co-ordinator
* Django Software Foundations manintain [django projects](https://www.djangoproject.com/), It is non-profit organization.
* Who uses django - Instagram, Google, Yahoo maps, Dropbox etc.
* It is first released in 2003 as an internal projects of [lawrence journal-world news](https://www2.ljworld.com/).
* Django is developed by **Adrian Holovati, Simon Willison**
* After testing this framework with high traffic in july 21, 2005 it published as an open source project.
* Django name cames from famous guitarist **Django Reinhardt**.
* Top 5 Features of Django
    * Very Fast
        * 95% works done by framework
    * Battery Included
    * Security
    * Scalable
    * Versatile
* Django has clear [documentation](https://docs.djangoproject.com/en/4.1/) and built in polling application as tutorial.

## Installation & Configuration

It is highly recommend that to install most recent stable version of django. Latest version may not be stable.

**Install Django 🤞🏻**

* `pip install django`
    * latest version will be installed
* `pip install django==x.x.x`
    * Specfic version will be installed

**Check Django is installed or not 🤞🏻**

* `python -m django --version`

To work with django first we've to understand  `django project` and `django application` terminology.

* Django project is a group of applications and configuration information.
    * Bank Project
        * Customer Application
        * Loan Application
        * Marketing Application
        * Insurence Application
* Application is responsible to perform particular task.

**Create Django Project 🤞**

* To create django project first you've to type `django-admin startproject ProjectName`
* After run this command django project structured will be look like this
    * ![django-project-structure](https://cutt.ly/VCxYFjz)
* Application is responsible to perform particular task.
    * `python manage.py startapp AppName`
    * ![django-app-structure](https://cutt.ly/6CYaiCq)
* Web server provides environment to run the the application.
    * to run the server type `python manage.py runserver`. Default server is `127.0.0.1:8000` but we can change the port also by typing `python manage.py runserver xxxx`

**Steps to Develop a Django Project 🤞**

* Create Project
* Create Application
* Install an application in the `settings.py` file
* Create view function in `views.py` to provide response
    * Every view function takes `request` as an input & return `response` as output.
* Define urlpattern for view function in `urls.py` file.
    * For every view function we've to provide separate urlpattern
    * By using this urlpattern user can send request.
* Run server
* Send the request

**How Server Response a Request 🤞🏻**

`127.0.0.1:8000/movies`

* First server will get requested via urlpattern
* Server opens `urls.py` file
* Server identifes the corresponding view function from `urls.py` file
* Server will execute the `view(model, template)` function and return response to the user 
