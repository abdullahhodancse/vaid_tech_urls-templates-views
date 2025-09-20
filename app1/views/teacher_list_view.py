
from app1.models.teachers_model import Teacher
from django.views.generic  import ListView,DetailView
from django.shortcuts import render
from django.db.models import Sum,Q



class teacher_list(ListView):   #class base view,
    model=Teacher
    template_name="teacher_list.html"
    context_object_name="teachers"




def total_salary_view(request):
    
    total_salary = Teacher.objects.aggregate(total=Sum('slary')) #aggerget use korle total sum payoa jay,ba aro math kora jai,loke

    
    return render(request, "total_salary.html", {"total_salary": total_salary})   



# Search teacher view
def search_teacher(request):
    query = request.GET.get("q")
    results = Teacher.objects.all()
    if query:
        results = results.filter(
            Q(name__icontains=query) |
            Q(department__name__icontains=query) |
            Q(subject__name__icontains=query)
        ).distinct()
    return render(request, "search_teacher.html", {"results": results, "query": query})

class teacher_details(DetailView):
    template_name="search_teacher.html"
    model=Teacher
    context_object_name="teacher_result"
