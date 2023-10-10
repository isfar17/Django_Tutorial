from django.urls import path
from . import views

app_name="my_app"

urlpatterns=[
    path("",views.homepage,name="homepage"),
    path("loginpage/",views.loginpage,name="loginpage"),
    path("restricted/",views.restricted,name="restricted"),
    path("user/<int:id>",views.user,name="user"),
    path("logout/",views.logout_user,name="logout_user"),
    path("registration/",views.registration,name="registration"),
    
]