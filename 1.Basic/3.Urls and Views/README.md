all the http response related functionalities are included in django.http
way 1:
1. write an index in firstapp.view
2. go to my_project.urls and import the firsapp.view
3. go to url_patterns and add the url:  path('firstapp',views.index,name="index")

Step 2:
1. write an index firstapp.view
2. Make a urls.py file in firstapp
2. go to firstapp.urls and import the view
4. go to url_patterns and add the url:  path('firstapp',views.index,name="index")
5. Go to  my_project.urls . import the views.
6. Add the views in urs.py by include() and path() function

We can also write views in urls.py file of my_project. So the basic here is to know how to route and connect views and urls.
