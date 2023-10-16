from .models import Demo
from django.forms import forms,ModelForm

class DemoForm(ModelForm): #model form will automatically generate forms for the model
    class Meta:
        model=Demo
        fields="__all__"
                    