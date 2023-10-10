steps:
```

e:\Django Tutorial\4. Django Admin\1. Admin setup\my_project>python manage.py makemigrations 
No changes detected

e:\Django Tutorial\4. Django Admin\1. Admin setup\my_project>python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

e:\Django Tutorial\4. Django Admin\1. Admin setup\my_project>python manage.py createsuperuser
Username (leave blank to use 'isfar'): Jubayer
Email address: testwithjubayer@gmail.com
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

e:\Django Tutorial\4. Django Admin\1. Admin setup\my_project>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 30, 2023 - 19:48:47
Django version 4.2.2, using settings 'my_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[30/Sep/2023 19:48:49] "GET / HTTP/1.1" 200 10664
Not Found: /favicon.ico
[30/Sep/2023 19:48:49] "GET /favicon.ico HTTP/1.1" 404 2114
[30/Sep/2023 19:48:53] "GET /admin HTTP/1.1" 301 0
[30/Sep/2023 19:48:53] "GET /admin/ HTTP/1.1" 302 0
[30/Sep/2023 19:48:53] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4181
```

without migrating if we try to make superuser, it will create error, because there has not been any models or tables made for users yet:
``` 
python manage.py createsuperuser

error: django.db.utils.OperationalError: no such table: auth_user

```
