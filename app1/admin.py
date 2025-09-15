# from django.contrib import admin
# from  app1.models import Account


# admin.site.register(Account)


from django.contrib import admin
from app1.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
   