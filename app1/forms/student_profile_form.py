from django import forms
from app1.models.student_model import Student

class student_pro_form(forms.ModelForm):
    class Meta:
        model=Student
        fields=['first_name','last_name','roll','reg','new_department','session','teaher','subjects','photo']
