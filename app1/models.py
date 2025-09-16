
from django.db import models
from django.contrib.auth.models import User




class Account(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    roll = models.IntegerField( null=True, blank=True,default=0000000)
    reg = models.IntegerField( null=True, blank=True,default=0000)
    department = models.CharField(max_length=100, null=True, blank=True)
    session = models.CharField(max_length=20, null=True, blank=True,default='2020-2021')

    def __str__(self):
       

        return self.user.username

    def save( self,*args,**kwargs):
        if self.roll is not None and self.roll<0:
            raise ValueError("Roll can not be negative")
        
        if self.reg is not None and self.reg<0:
            raise ValueError("Reg can not be negative")
        
        
        
        
        super().save(*args,**kwargs)



    