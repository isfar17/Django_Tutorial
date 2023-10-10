'''this is a custom made urls.py file created to route the views within the app. later we will
link it to the main project.urls file'''

from django.urls import path #copy from the project.urls file
from . import views # we are importing the views file from the same directory to access the functions

urlpatterns = [
    path('',views.index,name="index") # will show up at "/" in project.urls
]
