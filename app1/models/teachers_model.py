from django.db import models
from django.contrib.auth.models import User
from app1.models.departments_model import Department
from app1.models.subjects_model import Subject



class Teacher(models.Model):
   
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="teacher",null=True)
    name=models.CharField(null=True,max_length=20)
    slary=models.DecimalField(max_digits=10,decimal_places=2)  
    subject =models.ManyToManyField(Subject,related_name="teacher_sub")
    department=models.ForeignKey(Department,on_delete=models.CASCADE, related_name="Teachers")
    profile_image_base64 = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name
    