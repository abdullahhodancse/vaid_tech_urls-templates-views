from django.contrib import admin
from app1.models.departments_model import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=("id","name","created_at")
    search_fields=('name',)
    list_filter=("created_at",)
    ordering=("id",)
    list_per_page=20

