from django.core import validators
from django import forms
from .models import Student_Info,Parent_Info

class Student_edit(forms.ModelForm):
    class Meta:
        model=Student_Info
        fields = ['first_name','last_name','age','DOB','City']
        lables= {'first_name':'first_name','last_name':'last_name','age':'age','DOB':'DOB','City':'City'}
        error_messages = {
            'first_name':{'required':'Write first name please!'},
            'last_name':{'required':'Adnaav tak ree makda!'},
            'age':{'required':'Age tuzha baap taknar ka!'},
            'DOB':{'required':'vay kay ahe zhavnya!'},
            'City':{'required':'Kutla re tu !'}
        }