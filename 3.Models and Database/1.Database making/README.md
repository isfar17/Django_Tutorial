commands :

1. python manage.py migrate
2. add the app in installed app
3. python manage.py makemigrations app_name
4. python manage.py sqlmigrate app_name 001(the migration name (such as 00001) we want to update)
5. python manage.py migrate (without this, migration will fail)

migration folder is very important. whenever there is a change in the database, migration folder keeps track. and the latest 
migration file always depends on the previous ones to keep track. so by any chance if any migration file is deleted, or the one
upon which the last migration file is depended, databse will collaps. so keep in mind.