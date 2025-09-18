
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from .forms import UserRegistrationForm  # Make sure this is your form
from datetime import date
from django.contrib.auth.decorators import login_required
from app1.models import Student
from django.contrib.auth import login, authenticate

from django.db.models import Sum
from app1.models import Teacher
from django.views.generic  import ListView



# def signup(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             try:
#                 Student.objects.create(
#                 user=user,
#                 roll=form.cleaned_data.get('roll'),
#                 reg=form.cleaned_data.get('reg'),
#                 department=form.cleaned_data.get('department'),
#                 session=form.cleaned_data.get('session')
#             )
                
#             except ValueError as e:
#                 messages.error(request, str(e))
#                 user.delete()  # Optional: rollback user creation
#                 return redirect('signup')
        
            


#             # Create Account
            

#             # Auto-login
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)

#             messages.success(request, "Account created successfully! You are now logged in.")
#             return redirect('login')  # Or redirect to dashboard/home

#         else:
#             messages.error(request, "Signup unsuccessful. Please correct the errors below.")
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'app1.html', {'form': form, 'type': 'Signup', 'my_date': date.today()})


from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import date
from .forms import UserRegistrationForm

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Signal দ্বারা auto-created Student object get করা
            student = user.student

            # Form থেকে data assign করা
            student.roll = form.cleaned_data.get('roll')
            student.reg = form.cleaned_data.get('reg')
            student.department = form.cleaned_data.get('department')
            student.session = form.cleaned_data.get('session')

            # Save with ValueError handling
            try:
                student.save()
            except ValueError as e:
                messages.error(request, str(e))
                user.delete()  # rollback
                return redirect('signup')

            # Auto-login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

            messages.success(request, "Account created successfully! You are now logged in.")
            return redirect('login')

        else:
            messages.error(request, "Signup unsuccessful. Please correct the errors below.")
    else:
        form = UserRegistrationForm()

    return render(request, 'app1.html', {'form': form, 'type': 'Signup', 'my_date': date.today()})







@login_required
def login_view(request):
    try:
       student = request.user.student
    except Student.DoesNotExist:
        account = None  

    return render(request, 'login.html', {'student': Student})



#tortal satry od teacher

def total_salary_view(request):
    
    total_salary = Teacher.objects.aggregate(total=Sum('slary')) #aggerget use korle total sum payoa jay,ba aro math kora jai,loke

    
    return render(request, "total_salary.html", {"total_salary": total_salary})


class teacher_list(ListView):   #class base view,
    model=Teacher
    template_name="teacher_list.html"
    context_object_name="teachers"



class student_list(ListView):
    model=Student
    template_name="student.html"
    context_object_name="students"


