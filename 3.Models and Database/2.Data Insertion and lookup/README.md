steps to migrate and setup:
```
e:\Django Tutorial\3.Models and Database\2.Data Insertion and lookup\my_site>python manage.py migrate
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

e:\Django Tutorial\3.Models and Database\2.Data Insertion and lookup\my_site>python manage.py makemigrations my_app  
Migrations for 'my_app':
  my_app\migrations\0001_initial.py
    - Create model Base

e:\Django Tutorial\3.Models and Database\2.Data Insertion and lookup\my_site>python manage.py sqlmigrate my_app 0001
BEGIN;
--
-- Create model Base
--
CREATE TABLE "my_app_base" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(300) NOT NULL, "last_name" varchar(300) NOT NULL);
COMMIT;

e:\Django Tutorial\3.Models and Database\2.Data Insertion and lookup\my_site>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, my_app, sessions
Running migrations:
  Applying my_app.0001_initial... OK

e:\Django Tutorial\3.Models and Database\2.Data Insertion and lookup\my_site>

``` 

commands to enter data and pass it to database

``` 
e:\Django Tutorial\3.Models and Database\1.Database making\my_site>python manage.py shell
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.14.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from my_app.models import Base

In [2]: obj=Base(first_name="Jubayer",last_name="Isfar") #first way

In [3]: obj.save()

In [4]: Base.objects.all()
Out[4]: <QuerySet [<Base: Base object (1)>]>

In [5]: Base.objects.all()
Out[5]: <QuerySet [<Base: Base object (1)>]>

In [6]: Base.objects.create(first_name="Tariq", last_name="Zabir") #second way and better way
Out[6]: <Base: Base object (2)>

In [7]: Base.objects.bulk_create([Base(first_name="New",last_name="User"),Base(first_name="Mahir",last_name="Shafiq")])
Out[7]: [<Base: Base object (3)>, <Base: Base object (4)>]

In [8: data={"first_name": "Mohsin","last_name": "Khan"}

In [9]: Base.objects.create(**data) #Third way to save data from json format
Out[9]: <Base: Base object (3)>

```
