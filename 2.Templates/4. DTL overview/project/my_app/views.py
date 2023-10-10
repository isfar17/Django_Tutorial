from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello this is the index page. go to /first and /second for the page view")
def first(request):
    return render(request,"my_app/first.html")

def second(request):
    return render(request,"my_app/second.html")

def inherited(request):
    return render(request,"my_app/inherited.html")