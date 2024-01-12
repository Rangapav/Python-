from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    name = models.CharField(max_length=90)
    Category = [
        ('sel', 'select your gender'),
        ('Health', 'Health'),
        ('Electronics', 'Electronics'),
        ('Travel', 'Travel'),
        ('Education', 'Education'),
        ('Books', 'Books'),
        ('Others', 'Others')
    ]
    category = models.CharField(choices=Category, max_length=90)
    Date_of_Expense = models.DateField()
    Amount = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=90)




    def __str__(self):
        return self.name
