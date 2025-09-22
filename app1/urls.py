
from django.urls import path
from app1.views.student_list_view  import  student_list
from app1.views.student_login_singn_up import signup,login_view
from app1.views.teacher_list_view import total_salary_view,teacher_list,search_teacher,teacher_details
from app1.views.profile_both import profile_view,edit_view
from app1.views.log_out_both import log_out
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('reg/',signup,name='signup'), #normal for (FBV)
    path('login/', login_view, name='login'),
    path('salary/',total_salary_view,name='Total_salary'),
    path('teacher/',teacher_list.as_view(),name="teacher_list"),
    path('student/',student_list.as_view(),name="student_list"),
    path('search/',search_teacher,name='teacher_search'),
    path('teachers/<int:pk>/', teacher_details.as_view(), name='teacher_detail'),
    path('profile/',profile_view,name='profile'),
    path('edit/',edit_view,name='edit'),
    path('log_out/',log_out,name='log_out')

    
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# if settings.DEBUG:
