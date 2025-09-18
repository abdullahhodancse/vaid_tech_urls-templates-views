
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver











class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="student",null=True)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    roll = models.IntegerField( null=True, blank=True,default=0000000)
    reg = models.IntegerField( null=True, blank=True,default=0000)
    department = models.CharField(max_length=100, null=True, blank=True)
    session = models.CharField(max_length=20, null=True, blank=True,default='2020-2021')
    subjects = models.ManyToManyField('Subject', related_name='students', blank=True)
    teaher = models.ManyToManyField('Teacher', related_name='students', blank=True)
    

    # def __str__(self):
       

    #     return self.name if self.name else f"Student ID {self.id}"
    
    def __str__(self):
        if self.first_name or self.last_name:
            return f"{self.first_name or ''} {self.last_name or ''}".strip()
        return f"Student ID {self.id}"
   
        
   






    def save( self,*args,**kwargs):
        if self.roll is not None and self.roll<0:
            raise ValueError("Roll can not be negative")
        
        if self.reg is not None and self.reg<0:
            raise ValueError("Reg can not be negative")
        
        
        
        
        super().save(*args,**kwargs)

    @property    #ekhon html e full_name likhle e full name ddekhabe,,,,alada alada first_name /last_name likha lagbe na
    def full_name(self):
        return f"{self.name} ({self.roll})" if self.name else f"Student ID {self.id}"    
    


    @classmethod   #aita holo amar kono obkect er valus change korte use hoy,,
    def create_student(cls, name, roll, reg, department, session):
        student = cls(name=name, roll=roll, reg=reg, department=department, session=session)
        student.save()
        return student
    

    @staticmethod #aita moluto ekta ekta helping function,,,
    def is_roll_valid(roll):
        return roll >= 0
    



    @receiver(post_save, sender=User)  # user cteate hoiye sorasori profile creare hobe
    def create_student_or_teacher_profile(sender, instance, created, **kwargs):
        if created:
             #Example: automatically create a Student profile for every new user
            Student.objects.create(user=instance, first_name=instance.first_name)
        # You can also create Teacher if needed
        # Teacher.objects.create(user=instance, name=instance.username)
    
        


#subject model
class Subject(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name 
#department model
class Department(models.Model):
    name=models.CharField(max_length=100)  


    def __str__(self):
        return self.name 
    
#teacher model
class Teacher(models.Model):
   
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="teacher",null=True)
    name=models.CharField(null=True,max_length=20)
    slary=models.DecimalField(max_digits=10,decimal_places=2)  
    subject =models.ManyToManyField(Subject,related_name="teacher_sub")
    department=models.ForeignKey(Department,on_delete=models.CASCADE, related_name="Teachers")


    def __str__(self):
        return self.name
    









