from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('<str:data>',views.dynamic_index,name="dynamic_index"),
]
