from django.contrib import admin
from Admin.models import Admins

class AdminAdmin(admin.ModelAdmin):
    list_display=('Login_name','Login_password')

admin.site.register(Admins,AdminAdmin)
