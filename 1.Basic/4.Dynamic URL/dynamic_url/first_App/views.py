from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a home page")

def dynamic_index(request,data):
    return HttpResponse(f"You wrote {data} !")