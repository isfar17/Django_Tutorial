from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#this is a basic function that will show/render html text in web browser. We are using html text to show. So we use HttpResponse
def index(request):#it takes a request. Don't forget to use this parameter
    return HttpResponse("Hello this is the index call from my_app.views ")