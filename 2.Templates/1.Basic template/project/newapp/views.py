#render is used to import html files from templates
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def index_inside_folder(request):
    return render(request,"newapp/index.html")