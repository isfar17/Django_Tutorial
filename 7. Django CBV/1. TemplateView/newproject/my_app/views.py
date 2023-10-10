from django.shortcuts import render

from django.views.generic import TemplateView,FormView

# Create your views here.
class IndexView(TemplateView): #make a class and inherit templateview class
    template_name="my_app/index.html" 