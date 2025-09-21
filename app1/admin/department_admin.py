from django.contrib import admin
from app1.models.departments_model import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=("id","name","created_at")
    search_fields=('name',)
    list_filter=("created_at",)
    ordering=("id",)
    list_per_page=20


    def has_add_permission(self, request):
        return request.user.is_superuser   #shudu super user student add korte parbe
    

    def has_change_permission(self, request, obj =None):  #stuss  chage korte parbe
        return request.user.is_staff
    
    def has_delete_permission(self, request, obj = None): #stuff delete korte parbe
        if request.user.is_staff:
            return super().has_delete_permission(request, obj)

        return False
        
