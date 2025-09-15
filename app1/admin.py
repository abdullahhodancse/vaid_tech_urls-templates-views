# from django.contrib import admin
# from  app1.models import Account


# admin.site.register(Account)


from django.contrib import admin
from app1.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["roll", "session"]

    @admin.display(empty_value="???")  
    def session(self, obj):
        return obj.session
    

