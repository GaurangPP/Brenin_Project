from django import forms
from .models import Info

class InputForm(forms.Form):
    #class Meta:
    #    model = Info
    #    fields = ('name','age','email','number','query')
        
    name = forms.CharField(help_text="Enter Full Name",max_length=100)
    age = forms.IntegerField()
    email = forms.CharField(max_length=200)
    number = forms.IntegerField()
    query = forms.CharField(max_length=500)
