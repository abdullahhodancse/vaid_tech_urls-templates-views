from app1.models.student_model import Student
from django.views.generic  import ListView

class student_list(ListView):
    model=Student
    template_name="student.html"
    context_object_name="students"