from django.db import models
from django.contrib.auth.models import User


class UploadFfiles(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="file")
    file=models.FileField(upload_to='app1/media/general_file')

    time=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username}-{self.file.name}"