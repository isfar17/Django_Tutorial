from django.shortcuts import render



from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return HttpResponse("Hello this is the app index ")


def second(request):
    return HttpResponse("This is the second function") #this function redirects to any url of the website user wants,(not function)


def third(request,data):
    return HttpResponse(f"You typed {data}") 
# for example 1287.0.0.1/the url we want to go

def redirection_second(request):
    return HttpResponseRedirect(reverse("second"))
 
def redirection_third(request):
    data="This is a line from redirection third function"
    return HttpResponseRedirect(reverse("third",args=[data])) 