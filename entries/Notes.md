# Notes
 
Djanbo lecture notes: 

to create a project:

django-admin startproject PROJECT_NAME

Example: django-admin startproject Lecture3:
Lecture3  - folder:
manage.py use to execute commands in the django project
settings:  configuration settings for our project
urls.py: table of content for our web-application that I can visit

Applications: 
A project can contain several seperate applications:
python manage.py startapp NAME_OF_APP
views.py: what the user sees when they visit a particular route and what we decide what is rendered to the user

We need to install the app:
Go to settings.py:
INSTALLED_APPS:
add: NAME_OF_APP

FIrst create a view in views.py of the app

create a urls.py in the app 
from django.urls import path
from . import views
urlpatterns = [
	path("", views.index, name="index"

from django.urls import include, path

in urls.py of the project:
include:
path('NAME_OF_APP/', include('NAME_OF_PROJECT.urls


Django Data form