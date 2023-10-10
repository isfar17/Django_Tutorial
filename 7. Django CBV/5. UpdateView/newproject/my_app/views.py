from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView,FormView,CreateView,ListView,UpdateView

from .forms import DemoForm
from .models import Demo

# Create your views here.
class IndexView(TemplateView): #make a class and inherit templateview class
    template_name="my_app/index.html" 
    

class DemoFormView(FormView):
    
    template_name="my_app/form.html"
    
    form_class=DemoForm
    success_url=reverse_lazy('my_app:indexview') #reverse is used in function based views. And reverse_lazy for class based views
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class DemoCreateView(CreateView):
    #template name = "modelname_form.html"
    model=Demo
    fields="__all__"
    success_url=reverse_lazy("my_app:listview") #will take me to the /list where all data is listed
    
    #automatically saves the data into database,template name must be same as the model name, readme.md has more info
    
    
class DemoListView(ListView):
    #template name = "modelname_list.html"
    
    model=Demo
    
    context_object_name="all_data" #the name of the list we will be iterating through in html file.
    #html file should be same repetitive as model_list.html format
    
class UpdateDemoView(UpdateView):
    #we dont need any templates, it will share the same html file of create view
    #same as create view 
    model=Demo
    fields="__all__"
    success_url=reverse_lazy("my_app:listview") #will take me to the /list where all data is listed
