from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app1.models import Employee
from app1.forms import EmployeeList  # Assuming you have ExpenseForm in your forms.py
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User,auth # Import the logout function
import re

def home(request):
    return render(request,'app1/home.html')
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken. Please choose a different one.')
            return redirect('signin')

        # Check if the username is unique
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken. Please choose a different one.')
            return redirect('signin')

        # Check if the password meets the length requirement
        if len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return redirect('signin')

            if not re.search(r'[!@#$%^&*()_+{}|:"<>?]', password1):
                messages.error(request, 'Password must contain at least one symbol.')
                return redirect('signin')

                if not re.search(r'[A-Z]', password1):
                    messages.error(request, 'Password must contain at least one capital letter.')
                    return redirect('signin')



        data = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username,
                                        password=password1)
        data.save()
        return redirect('login')

    return render(request, 'app1/register.html')

# Modified the name of the login view function to avoid conflicts with the login template
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
                messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'app1/login.html')

class EmpListView(ListView):
    model = Employee
    # template_name = 'app1/expense_list.html'  # Add the template name

class EmpCreateView(CreateView):
    model = Employee
    fields='__all__'
    success_url = reverse_lazy('Employee')

class EmpUpdateView(UpdateView):
    model = Employee
    fields='__all__'
    success_url = reverse_lazy('Employee')

class EmpDeleteView(DeleteView):
    model = Employee
    fields='__all__'
    success_url = reverse_lazy('Employee')  # Update with your actual URL name

def employee_list(request):
    queryset = Employee.objects.all()

    # Check if a search query is provided
    search_query = request.GET.get('query')
    if search_query:
        # Filter the queryset to include only employees whose names match the search query
        queryset = queryset.filter(name__icontains=search_query)

    context = {'employees': queryset}
    return render(request, 'app1/employee_list.html', context)
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        username = request.user.username
        return render(request, 'app1/logout.html', {'username': username})
