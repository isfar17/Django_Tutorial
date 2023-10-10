from django import forms

class DemoForm(forms.Form):
    name=forms.CharField(max_length=200)
    age=forms.IntegerField()
    