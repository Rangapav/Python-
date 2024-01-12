from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app1.models import Expense
from app1.forms import ExpenseForm  # Assuming you have ExpenseForm in your forms.py
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User,auth # Import the logout function


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
            return redirect('Expense')
        else:
                messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'app1/login.html')

class ExpListView(ListView):
    model = Expense
    # template_name = 'app1/expense_list.html'  # Add the template name

class ExpCreateView(CreateView):
    model = Expense
    fields='__all__'
    success_url = reverse_lazy('Expense')

class ExpUpdateView(UpdateView):
    model = Expense
    fields='__all__'
    success_url = reverse_lazy('Expense')

class ExpDeleteView(DeleteView):
    model = Expense
    fields='__all__'
    success_url = reverse_lazy('Expense')  # Update with your actual URL name

def logout_view(request):
    logout(request)
    return redirect('login')
