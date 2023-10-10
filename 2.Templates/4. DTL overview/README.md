steps to create templates:

1. first make templates/same_app_name_directory
2. then create templates 
3. connect the app.config in settings.py file, the name is taken from app.py file
4. go to views.py file and make views
5. make a urls.py file in my_app then connect urls there importing views
6. lastly connect the urls in project.urls file

django template language basics:
1. extends command is same as jinja
2. for/if condition is same as jinja.
3. url and routing is different
4. block naming is different, such as {  block title  endblock}
5. some cases such as function calling is different , in dtl, () is not used
6. commenting and include block is same

