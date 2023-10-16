from . import  views
from django.urls import path
from .views import ShowData

from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns=[
    path("",views.index,name="index"),
    path("list",ShowData.as_view(),name="showdata")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#django has problem serving media files in production mode. read: https://stackoverflow.com/questions/39051206/how-to-serve-media-files-on-django-production-environment