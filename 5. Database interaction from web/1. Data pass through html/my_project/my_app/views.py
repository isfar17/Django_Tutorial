from django.shortcuts import render,redirect
from django.urls import reverse


from . import models

# Create your views here.
def index(request):
    all_data={
        "data":models.People.objects.all()
    }
    return render(request,"my_app/index.html",context=all_data)

def form(request):
    
    if request.POST:
        
        print(request.POST)
        name=request.POST["name"]
        age=int(request.POST["age"])
        
        try:
            models.People.objects.create(name=name,age=age)
            return redirect(reverse('my_app:index'))
        except:
            return redirect(reverse('my_app:form'))
            
    return render(request,"my_app/form.html")