
from django.urls import path
from app1.views  import signup ,login_view

urlpatterns=[
    path('reg/',signup,name='singup'), #normal for (FBV)
    path('login/', login_view, name='login'),
    
 ]
