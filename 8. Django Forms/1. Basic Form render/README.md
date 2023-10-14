make forms.py file and make a form class. then render the form in views.py file.
next go to views and write the codes. in the html files do not forget to add the forms and csrf token
django forms doesnt have submit field.so we have to add it manually. After that get data in index. validate data and send user to
thankyou.html file

'''
[14/Oct/2023 11:44:53] "GET / HTTP/1.1" 200 1000
Not Found: /favicon.ico
[14/Oct/2023 11:44:54] "GET /favicon.ico HTTP/1.1" 404 2443
{'name': 'Jubayer', 'age': 20, 'bool_field': True}
Jubayer
[14/Oct/2023 11:45:56] "POST / HTTP/1.1" 302 0
[14/Oct/2023 11:45:56] "GET /form HTTP/1.1" 200 246
'''