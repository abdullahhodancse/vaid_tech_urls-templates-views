
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from .forms import UserRegistrationForm  # Make sure this is your form
from datetime import date
from django.contrib.auth.decorators import login_required
from app1.models import Account
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                Account.objects.create(
                user=user,
                roll=form.cleaned_data.get('roll'),
                reg=form.cleaned_data.get('reg'),
                department=form.cleaned_data.get('department'),
                session=form.cleaned_data.get('session')
            )
                
            except ValueError as e:
                messages.error(request, str(e))
                user.delete()  # Optional: rollback user creation
                return redirect('signup')
        
            


            # Create Account
            

            # Auto-login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

            messages.success(request, "Account created successfully! You are now logged in.")
            return redirect('login')  # Or redirect to dashboard/home

        else:
            messages.error(request, "Signup unsuccessful. Please correct the errors below.")
    else:
        form = UserRegistrationForm()

    return render(request, 'app1.html', {'form': form, 'type': 'Signup', 'my_date': date.today()})





@login_required
def login_view(request):
    try:
        account = request.user.account
    except Account.DoesNotExist:
        account = None  

    return render(request, 'login.html', {'account': account})
   