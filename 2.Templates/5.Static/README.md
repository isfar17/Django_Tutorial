adding static file is easy.

2 ways to create static folder:

1. The static folder for the apps themselves
2. static folder for the whole project

by default, django searches for static folder in project/static folder, then if not found then in the static folders of
the apps. so we will create two static folders, one outside the app, one inside the app with a subfolder named after the app
to avoid collision while searching for static files.

one thing is that most of the work here is in the html files and in settings.py file. so if we connect static folder inside the app,
and then run the program, it will work. But then what if we want outer static directory for the whole project.

###
Deployment¶
django.contrib.staticfiles provides a convenience management command for gathering static files in a single directory so you can serve them easily.

Set the STATIC_ROOT setting to the directory from which you’d like to serve these files, for example:

STATIC_ROOT = "/var/www/example.com/static/"
Run the collectstatic management command:

$ python manage.py collectstatic
This will copy all files from your static folders into the STATIC_ROOT directory.