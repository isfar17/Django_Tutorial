There are two different terminologies to define project and app. A project is the collection of apps. And an app is the part of a 
project. Let's imagine Facebook. Here facebook is the project where messenger,groups,marketplace,videos are different apps. so an app
is the collection of some urls and codes. On the other hand, a project is the collection of everything, all the configuration and 
management is done through the project.

1. Create a project - django-admin startproject my_site
2. go to project
3. create an app - python manage.py startapp my_app
4. create a view function in my_app.views
5. create a urls.py file in my_app, setup urls for the functions in views
6. go to my_site.urls and import the urls and views of my_app and connect them