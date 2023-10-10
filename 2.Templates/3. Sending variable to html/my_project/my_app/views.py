from django.shortcuts import render

# Create your views here.
def index(request):
    data={
        "text":"this is a sample text",
        "number":2,
        "list":[1,2,3,4,5,"nine","ten"],
    }
    return render(request,"my_app/index.html",context=data) # the dictionary is already passed. we need to type keys to access in html