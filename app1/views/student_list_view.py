from app1.models.student_model import Student
from django.views.generic  import ListView
from app1.models.departments_model import Department

class student_list(ListView):
    model=Student
    template_name="student.html"
    context_object_name="students"


    def get_queryset(self):
        queryset = super().get_queryset()
        department_id = self.request.GET.get("department")
        if department_id:
            queryset = queryset.filter(new_department_id=department_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Department.objects.all()
        return context





    
    
