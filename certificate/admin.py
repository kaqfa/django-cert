from django.contrib import admin
from .models import Certificate, Legalization
# Register your models here.


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['certificate_number', 'student', 'gpa', 'thesis_title']


class LegalizationAdmin(admin.ModelAdmin):
    list_display = ['uploaded_file', 'qr_code', 'submitted_at', 'submitter']


admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Legalization, LegalizationAdmin)