1. setup the project and app, make urls.py file, make templates/my_app and create all the html files,register the app in settings.py file
2. go to views.py file and write the basic views. just redirect to the html files. go to urls.py and setup urls. Also dont forget to
 setup the app_name variable as we will use it to redirect user. go to project.urls and connect the urls. lastly check if all the url runs fine.

3. Next go to models.py file and make the Model. after that go to index.html and form.html to write forms and basic index data. After
that go to terminal and run all the migrations command.

4. after successfully running everything, go to database file to check if the table was created. if yes then go to views.py file.
Setup all the views. in index.html file import model and send all the data in dictionary format. Next in form function, render the
request data, and save the field data in variables. last try to save it in model and redirect user as per input. 

5. finally run the server and check if all works fine.

request form print:
[12/Oct/2023 12:45:32] "GET / HTTP/1.1" 200 914
[12/Oct/2023 12:46:31] "GET /form HTTP/1.1" 200 1317
<QueryDict: {'csrfmiddlewaretoken': ['mH8M9Qo7mJe0c6j5m1h6AHG3ta5SX2hwjgMl5yB3l1syYOsY4eHKjnncVP8LvEbF'], 'name': ['Anna Hen'], 'age': ['30']}>
[12/Oct/2023 12:46:53] "POST /form HTTP/1.1" 302 0
[12/Oct/2023 12:46:53] "GET / HTTP/1.1" 200 941
