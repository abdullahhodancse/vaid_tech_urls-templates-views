

from django.contrib import admin
from app1.models.student_model import Student
from app1.models.subjects_model import Subject

class SubjectInline(admin.TabularInline):   #jokhon noton student add korte jabo ek epage thek student add korte parbo
    model = Subject
    extra = 1   

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'roll', 'reg','photo','document')
    inlines = [SubjectInline]


    class Media:   #use the 
        css={
            'all':('css/admin_custom.css',)
        }
        js=('js/admin_custoom.js',)
      


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'student')


