
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from ..forms import UserRegistrationForm  # Make sure this is your form
from datetime import date
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from app1.models.student_model import Student









from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import date
from ..forms import UserRegistrationForm

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # signal diya auto profile banano
            student = user.student

            # from theke daya ana
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



#









