
from django.db import models


class Subject(models.Model):
    name=models.CharField(max_length=100)
    student = models.ForeignKey('app1.Student', on_delete=models.CASCADE, related_name='studen_subjects',null=True)


    def __str__(self):
        return self.name 