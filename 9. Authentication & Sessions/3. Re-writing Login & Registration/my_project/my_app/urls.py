from django.urls import path
from . import views

app_name='my_app'

urlpatterns=[
    path('',views.index,name='index'),
    path('page1/',views.page1,name='page1'),
    path('page2/',views.page2,name='page2'),
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_page,name='logout_page'),
    path('register/',views.register,name='register'),
    ]