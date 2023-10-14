from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from django.urls import reverse
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("Hello World. Go to accounts/login for login and /signup/ for signing up")



def signup(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            user_finder=User.objects.get(username=username) 
            print(user_finder)
            if user_finder is not None:
                print("User found. Registration failed")
                return redirect(reverse("my_app:signup"))
        except:
            User.objects.create_user(username=username,password=password)
            print("user created")
            return redirect('/accounts/login')
    return render(request,'registration/signup.html')