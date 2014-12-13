from django.contrib import admin
from .models import Student, Graduation
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['nim', 'name', 'phone', 'email', 'status', 'graduation']


class GraduationAdmin(admin.ModelAdmin):
    list_display = ['period', 'grad_date', 'venue']


admin.site.register(Student, StudentAdmin)
admin.site.register(Graduation, GraduationAdmin)