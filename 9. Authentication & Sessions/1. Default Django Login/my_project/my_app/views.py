from django.shortcuts import redirect, render


from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("Hello World. Go to accounts/login for logging in")



