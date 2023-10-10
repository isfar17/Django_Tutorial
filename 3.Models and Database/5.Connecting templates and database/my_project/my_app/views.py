from django.shortcuts import render
from .models import People
# Create your views here.
def index(request):
    #data from DJANGO TO HTML has to be passed MUST IN DICTIONARY FORMAT
    context={
        "data" : People.objects.all()
    }
    return render(request,"my_app/index.html",context=context) #must pass data through context variable