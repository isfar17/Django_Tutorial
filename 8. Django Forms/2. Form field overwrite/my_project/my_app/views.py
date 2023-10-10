from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import Form

# Create your views here.

def index(request):
    form=Form()
    if request.method=="POST":
        form=Form(request.POST) #pass the post data in form class to let django check the validations
        if form.is_valid():
            print(form.cleaned_data)
            name=form.data["name"] #storing form data
            print(name)
        return redirect(reverse("my_app:thankyou"))
    return render(request,"my_app/index.html",{"form":form})


def thankyou(request):
    return render(request,"my_app/thankyou.html")
