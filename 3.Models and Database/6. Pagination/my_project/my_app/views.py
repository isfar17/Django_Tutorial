from django.shortcuts import render

from django.core.paginator import Paginator
from .models import Demo
from faker import Faker #(worked with faker to create data first)
# Create your views here.
def index(request):
    
    data=Demo.objects.all() # get the data from database
    
    paginate=Paginator(data,10) #put the result into paginator and seperate the result
    
    page_num=request.GET["page"]
    
    page=paginate.get_page(page_num) #get any page from the paginator, we pass it in url and get by request.
    
    return render(request,'my_app/paginate.html',
                  context={
                      "page":page #sand the paginate data into website 
                      })