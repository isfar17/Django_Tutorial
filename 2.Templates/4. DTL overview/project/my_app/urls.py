from django.urls import path
from . import views

app_name="my_app"

urlpatterns=[
    path('',views.index,name="index"),
    path('first',views.first,name="first"),
    path('second',views.second,name="second"),
    path('inherited',views.inherited,name="inherited"),
]