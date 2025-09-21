from django import forms
from app1.models.teachers_model import Teacher

class Teacher_pro_form(forms.ModelForm):

    class Meta:
        model=Teacher
        fields=['name','slary','subject','department']
