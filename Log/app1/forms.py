from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app1.models import Employee

class EmployeeList(forms.ModelForm):
     class Meta:
         model=Employee
         fields='__all__'
