from django.contrib import admin
from Course.models import Courses

class CourseAdmin(admin.ModelAdmin):
    list_display=('Course_Name','Course_Fees','Course_Durations')

admin.site.register(Courses,CourseAdmin)
