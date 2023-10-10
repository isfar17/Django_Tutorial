from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('second',views.second,name="second"),
    path('third/<str:data>',views.third,name="third"),
    path('second_redirect',views.redirection_second,name="redirection_second"),
    path('third_redirect',views.redirection_third,name="redirection_third"),
]
