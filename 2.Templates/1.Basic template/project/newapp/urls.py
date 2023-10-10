from . import views

from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('folder',views.index_inside_folder,name="index_inside_folder"),
]
