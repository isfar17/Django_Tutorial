from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"my_app/index.html")


def page1(request):
    return HttpResponse("This is the page 1")

@login_required(login_url='/login/')
def page2(request):
    return HttpResponse("This is the page 2, You need to login before you can see this page")
 
def login_page(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        
        query=User.objects.filter(username=username).first()
        
        if not query:
            return redirect(reverse('my_app:login_page'))

        user=authenticate(username=username,password=password)
        if user is None:
            return redirect(reverse("my_app:login_page"))
        login(request,user)
        print('login successful')
        return redirect(reverse("my_app:index"))
        
    return render(request,'my_app/login.html')

def logout_page(request):
    logout(request)
    
    return redirect(reverse('my_app:index'))

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        print(first_name,last_name,username,password)
        
        query=User.objects.filter(username=username).first()
        if query is None:
            User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password)
            print("User created successfully")
            return redirect(reverse('my_app:login_page'))
    return render(request,'my_app/register.html')