from django.contrib import admin
from .models import Department, Course
# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'faculty', 'status']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'status', 'department']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)