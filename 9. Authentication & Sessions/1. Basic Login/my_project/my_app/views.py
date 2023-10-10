from django.shortcuts import redirect, render
#dont need to remember. go to google and search for it.
from django.contrib.auth import login,authenticate,logout,user_logged_in
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
def homepage(request):
    return render(request,"my_app/homepage.html")


def loginpage(request):
    if request.method =="POST":
        name=request.POST["name"]
        password=request.POST["password"]
        
        result=User.objects.filter(username=name,password=password)
        
        if result is None:
            print("No user found")
            return redirect(reverse("my_app:loginpage"))
        else:
            #optional, this authenticate function verfies user details, we can skip this  one too
            
            result=authenticate(username=name,password=password)
            if result is None:
                return redirect(reverse("my_app:loginpage"))
            else:
                login(request,result)
                return redirect(reverse("my_app:homepage"))
            
    return render(request,"my_app/loginpage.html")

def logout_user(request):
    logout(request)
    return redirect(reverse("my_app:loginpage"))

@login_required
def restricted(request):
    return render(request,"my_app/restricted.html")

@login_required
def user(request,id):#we dont need to specify type here, we will set it in the urls.py file
    if request.user.id == id:  
        return render(request,"my_app/user.html")
    else:
        return redirect(reverse("my_app:homepage"))


