from django.db import models

class Student(models.Model):
    assignment_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    roll_no = models.CharField(max_length=10, primary_key=True)  # Change to CharField
    assignment1 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    assignment2 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    assignment3 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    assignment4 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    assignment5 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    assignment6 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    class Meta:
        verbose_name = 'Python Student'
        verbose_name_plural = 'Python Students'

class DataStructuresStudent(models.Model):
    assignment_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    roll_no = models.CharField(max_length=10, primary_key=True)  # Change to CharField
    assignment1 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    assignment2 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    assignment3 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    assignment4 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    assignment5 = models.CharField(max_length=3, choices=assignment_choices, default='no')
    assignment6 = models.CharField(max_length=3, choices=assignment_choices, default='no')
