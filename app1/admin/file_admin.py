from django.contrib import admin
from app1.models.fileUp_model import UploadFfiles

# @admin.register(UploadFfiles)
# class File_Upload_Admin(admin.ModelAdmin):
#     list_display=("id","name","created_at")
#     search_fields=('name',)
#     list_filter=("created_at",)
#     ordering=("id",)
#     list_per_page=20

admin.site.register(UploadFfiles)