 command for starting project:

 ```
E:\Django Tutorial>cd "e:\Django Tutorial\1.Basic\1.Creating a project"

e:\Django Tutorial\1.Basic\1.Creating a project>django-admin startproject my_site

e:\Django Tutorial\1.Basic\1.Creating a project>cd my_site

e:\Django Tutorial\1.Basic\1.Creating a project\my_site>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.

Run 'python manage.py migrate' to apply them.
September 18, 2023 - 22:01:41
Django version 4.2.2, using settings 'my_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


```
or we could specify the port :
```
e:\Django Tutorial\1.Basic\1.Creating a project\my_site>python manage.py runserver
```