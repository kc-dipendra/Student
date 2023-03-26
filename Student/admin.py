from django.contrib import admin
from Student.models import Students

class StudentAdmin(admin.ModelAdmin):
    list_display=('Name','Roll','Age','Address','Phone')

admin.site.register(Students,StudentAdmin)
