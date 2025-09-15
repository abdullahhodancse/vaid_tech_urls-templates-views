
from django.urls import path
from app1.views  import signup

urlpatterns=[
    path('reg/',signup,name='singup'), #normal for (FBV)
#     path('reg/'singup.as_view(),name='singup'),  # for (CBV)
#     path('reg/<int:user_id>/'singup, name='singup'), #int parameter diya 
#     path('reg/<slug:slug>/'singup, name='singup'), #string 
#     path('reg/<int:user_id>/<slug:slug>/'singup, name='singup') #multiple
 ]
