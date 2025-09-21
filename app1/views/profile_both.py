from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app1.models.student_model import Student
from app1.models.teachers_model import Teacher
from app1.forms.student_profile_form import student_pro_form
from app1.forms.teacher_profile_forms import Teacher_pro_form

@login_required

def profile_view(request):
    user=request.user
    if hasattr(user,'student'):
        profile=user.student
        profile_type='student'
    elif hasattr(user,'teacher'):
        profile=user.teacher
        profile_type='teacher'  

    else:
        profile=None
        profile_type=None

    context = {'profile':profile, 'profile_type':profile_type}   
    return render(request, 'profile.html',context)      



@login_required
def edit_view(request):
    user=request.user
    if hasattr(user,'student'):
        profile=user.student
        form_class= student_pro_form

    elif hasattr(user,'teacher') :
        profile=user.teacher
        form_class= Teacher_pro_form  

    else:
        return redirect('profile')   


    if request.method=='POST':
        form=form_class(request.POST,instance=profile) 
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=form_class(instance=profile)

    return render(request,'edit.html',{'form':form})    