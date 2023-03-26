from django.contrib import admin
from Teacher.models import Teachers

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('Teacher_Name','Teacher_Education','Teacher_Subject')

admin.site.register(Teachers,TeacherAdmin)
