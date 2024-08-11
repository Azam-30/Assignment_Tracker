# admin.py
from django.contrib import admin
from .models import Student,DataStructuresStudent

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'assignment1', 'assignment2', 'assignment3', 'assignment4', 'assignment5', 'assignment6')
    list_filter = ('assignment1', 'assignment2', 'assignment3', 'assignment4', 'assignment5', 'assignment6')
    search_fields = ('roll_no',)
    

@admin.register(DataStructuresStudent)
class DataStructuresStudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'assignment1', 'assignment2', 'assignment3', 'assignment4', 'assignment5', 'assignment6')
    list_filter = ('assignment1', 'assignment2', 'assignment3', 'assignment4', 'assignment5', 'assignment6')
    search_fields = ('roll_no',)
