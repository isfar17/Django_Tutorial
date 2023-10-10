from django import forms

class Form(forms.Form):
    name=forms.CharField(label="Input your name",max_length=200)
    age=forms.IntegerField()
    bool_field=forms.BooleanField(label="Do you want to join django club?")

    
    