
from django.urls import path
from app1.views.student_list_view  import  student_list
from app1.views.student_login_singn_up import signup,login_view
from app1.views.teacher_list_view import total_salary_view,teacher_list

urlpatterns=[
    path('reg/',signup,name='singup'), #normal for (FBV)
    path('login/', login_view, name='login'),
    path('salary/',total_salary_view,name='Total_salary'),
    path('teacher/',teacher_list.as_view(),name="teacher"),
    path('student/',student_list.as_view(),name="teacher")
    
    
 ]
