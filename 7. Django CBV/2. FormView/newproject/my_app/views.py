from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView,FormView

from .forms import DemoForm
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