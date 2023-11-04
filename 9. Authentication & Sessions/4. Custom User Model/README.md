if we use User model instead of CustomUser after all the modification we will get this error:
AttributeError at /login/
Manager isn't available; 'auth.User' has been swapped for 'my_app.CustomUser'