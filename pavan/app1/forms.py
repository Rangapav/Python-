
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
