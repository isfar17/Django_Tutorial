from django.shortcuts import render,redirect
from .models import Demo
from .forms import DemoForm

from django.views.generic import ListView
# Create your views here.
def index(request):
    form=DemoForm()
    if request.method=="POST":
        form=DemoForm(request.POST)
        name=request.POST["name"]
        address=request.POST["address"]
        image=request.FILES["image"]
        try:
            Demo.objects.create(name=name,address=address,image=image)
        except:
            return redirect("/")
        return redirect("/") #redirect / means to redirect to same site by refreshing
    return render(request,"my_app/index.html",context={"form":form})

class ShowData(ListView):
    model=Demo
    #html file format="modelname_list.html"
    
    context_object_name="all_data" #by default context will take the name of the model, we can change here