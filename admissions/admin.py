from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Teacher

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'fathername', 'classname','contact']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'exp', 'subject','contact']

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)