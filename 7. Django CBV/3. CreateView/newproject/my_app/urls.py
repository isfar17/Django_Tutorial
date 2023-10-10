from django.urls import path
from . import views

app_name="my_app"

urlpatterns=[
    path("",views.IndexView.as_view(),name="indexview"),
    path("form",views.DemoFormView.as_view(),name="formview"),
    path("create",views.DemoCreateView.as_view(),name="createview"),
        ]   