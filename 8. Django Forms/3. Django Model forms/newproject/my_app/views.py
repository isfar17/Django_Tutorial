from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.
def index(request):
    return render(request,"my_app/index.html")


def form(request):
    form=ReviewForm()
    if request.method=="POST":
        form=ReviewForm(request.POST)
        
        name=form.data["name"]
        stars=form.data["stars"]
        print(name,stars)
    if form.is_valid():
        form.save() #automatically form will check the validation and save it to the model
        return redirect(reverse("my_app:index"))
    return render(request,"my_app/form.html",context={"form":form})