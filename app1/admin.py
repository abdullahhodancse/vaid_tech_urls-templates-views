from django.contrib import admin
from  app1.models import Account


admin.site.register(Account)






# from django.contrib import admin
# from app1.models import Account

# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ["roll", "session"]

#     @admin.display(empty_value="???")  
#     def session(self, obj):
#         return obj.session


    


# from django.contrib import admin
# from app1.models import Account
# class AccountAdmin(admin.ModelAdmin):
#     fields=["roll"]


# class accuntAdmin(admin.ModelAdmin):
#     exclude=["session"]   


# from django.contrib import admin
# from  app1.models import Account

# class AccountAdmin(admin.ModelAdmin):
#     fields=['roll', 'reg','department']

# admin.site.register(Account)



# from django.contrib import admin


# class FlatPageAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (
#             None,
#             {
#                 "fields": ["url", "title", "content", "sites"],
#             },
#         ),
#         (
#             "Advanced options",
#             {
#                 "classes": ["collapse"],
#                 "fields": ["registration_required", "template_name"],
#             },
#         ),
#     ]