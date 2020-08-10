# django-portfolio
A tutorial 

### Notes
`Development Environment`: *`/Django-Portfolio/`* This is the main directory for the project.  

`Virtual Environment`: *`/Django-Portfolio/venv`* This is directory used to manage dependencies.  

Command to make virtual env with `venv`:  

    $ python3 -m venv venv  

Command to activate virtual env:  

    $ source venv/bin/activate


Once activated, install Django

    (venv) $ pip install Django

To create project:

    $ django-admin startproject personal_portfolio

To start developent server:  

    $ python manage.py runserver


## Django Web Application is a project made with smaller applications

1.  Create a new app with this command

        $ python manage.py startapp hello_world

2. Make sure to install apps in your project. In `personal_portfolio/settings.py` add the following line of code under INSTALLED_APPS:

        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ->    'hello_world',
        ]

3. Create a View and view function that renders html

        from django.shortcuts import render

        def hello_world(request):
            return render(request, 'hello_world.html', {})

4. Create the HTML template inside the app `hello_world/templates/hello_world.html` 

5. Create the urls module for the application

        $ touch hello_world/urls.py
- Import the path object and apps view modules
- Create a list of URL patterns and view objects:

        from django.urls import path
        from hello_world import views

        urlpatterns = [
            path('', views.hello_world, name='hello_world'),
        ]
    
6. Hook up URLs from application to main URLs in project
- Inside `personal_portfolio/urls.py` add: 

        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('hello_world.urls')),
        ]
