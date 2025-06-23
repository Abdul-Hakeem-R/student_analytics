from django.contrib import admin
from .models import Student, Subject, Test, Result

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'roll_number')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'test_type', 'date', 'total_marks')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'test', 'marks_scored')
