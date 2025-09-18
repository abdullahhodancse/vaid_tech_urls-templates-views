
from app1.models.teachers_model import Teacher
from django.views.generic  import ListView
from django.shortcuts import render
from django.db.models import Sum


class teacher_list(ListView):   #class base view,
    model=Teacher
    template_name="teacher_list.html"
    context_object_name="teachers"




def total_salary_view(request):
    
    total_salary = Teacher.objects.aggregate(total=Sum('slary')) #aggerget use korle total sum payoa jay,ba aro math kora jai,loke

    
    return render(request, "total_salary.html", {"total_salary": total_salary})    