from django.contrib import admin
from application.models import StudentModel

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','fee']
admin.site.register(StudentModel,StudentAdmin)