from django.contrib import admin
from .models import Transcript
# Register your models here.


class TranscriptAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'grade', 'status']


admin.site.register(Transcript,TranscriptAdmin)