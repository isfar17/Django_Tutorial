basic commands to setup everything outside of project"
```
e:\Django Tutorial\3.Models and Database\4. Update and Delete data\my_project>cd "e:\Django Tutorial\3.Models and Database\5.Connecting templates and database"

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database>django-admin startproject my_project    

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database>mkdir image

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database>type nul >README.md

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database>cd my_project

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project>python manage.py startapp my_app

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project>cd my_app

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project\my_app>mkdir "templates/my_app"

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project\my_app>type nul >urls.py

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project\my_app>cd "templates/my_app"    

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project\my_app\templates\my_app>type nul >"index.html"

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project\my_app\templates\my_app>cd ..

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project\my_app\templates>cd..

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project\my_app>cd..

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project>  
```

migrations and database setup:
``` 
e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project>python manage.py makemigrations
Migrations for 'my_app':
  my_app\migrations\0001_initial.py
    - Create model People

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project>python manage.py sqlmigrate my_app 0001
BEGIN;
--
-- Create model People
--
CREATE TABLE "my_app_people" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "age" integer NOT NULL, "birthdate" date NOT NULL);
COMMIT;

e:\Django Tutorial\3.Models and Database\5.Connecting templates and database\my_project>python manage.py migrate               
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, my_app, sessions
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
  Applying my_app.0001_initial... OK
  Applying sessions.0001_initial... OK

```

