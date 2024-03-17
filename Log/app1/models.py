from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

class Employee(models.Model):
    name = models.CharField(max_length=90)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    DESIGNATION_CHOICES = [
        ('HR', 'HR'),
        ('Manager', 'Manager'),
        ('Sales', 'Sales'),
        ('Developer', 'Developer'),
        ('Others', 'Others')
    ]
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES)
    mobile_no = models.CharField(max_length=15)
    COURSE_CHOICES = [
        ('CSE', 'Computer Science and Engineering'),
        ('BSC', 'Bachelor of Science'),
        ('IT', 'Information Technology'),
        ('BCOM', 'Bachelor of Commerce'),
        ('CA', 'Chartered Accountancy'),
        ('MBA', 'Master of Business Administration')
    ]
    email = models.EmailField()
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
