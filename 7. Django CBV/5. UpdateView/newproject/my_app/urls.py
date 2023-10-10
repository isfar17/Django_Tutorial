from django.urls import path
from . import views

app_name="my_app"

urlpatterns=[
    path("",views.IndexView.as_view(),name="indexview"),
    path("form",views.DemoFormView.as_view(),name="formview"),
    path("create",views.DemoCreateView.as_view(),name="createview"),
    path("list",views.DemoListView.as_view(),name="listview"),
    path("update/<int:pk>",views.UpdateDemoView.as_view(),name="updateview"), #here by default we have to pass primary key
        ]   