from django.core import validators
from django import forms 
from . models import Addharno,Student


class Adharform(forms.ModelForm):
    class Meta:
        model=Addharno
        fields=['addharno']
        widgets={
            'addharno':forms.TextInput(attrs={'class':'form-control'}),
           
        }
        
class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields=['Name','Email','Mobile','Age','Address','Addharno']
      