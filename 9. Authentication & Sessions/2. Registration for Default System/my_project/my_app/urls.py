from django.urls import path
from . import views

app_name="my_app"

urlpatterns=[ 
    path("",views.homepage, name="homepage" ),
    path("signup",views.signup,name="signup"),
    ]