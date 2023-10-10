make migrations anhd create super user. Then go to the admin panel and create some users. Then write login functions to work with
 that.


username:jubayer
password: NewPass123

here are the  Choices : 

date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, last_login, last_name, logentry, password, 
user_permissions, username

these are the pre defined attributes we can access/user from the models or to use when logging in/registration.

functions are:

login page
homepage (login/logout function wil be shown if user is authenticated or not)
restricted page, can be accessed by any of the user who is logged in( blog creation page)
userpage(can only be accessed by the user that has the permission,such as:own profile page,settings)


in the registration process, its very similar to login, just some additional checking required and redirection. Easy as flask.