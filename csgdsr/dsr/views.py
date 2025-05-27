from django.shortcuts import render, redirect
from .forms import CustomSignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# dsr/views.py

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = CustomSignupForm()
    return render(request, 'dsr/signup.html', {'form': form})



def home_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if not remember:
                request.session.set_expiry(0)  # session expires on browser close

            return redirect('dashboard')  # or wherever you want to redirect after login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'dsr/home.html')

def dashboard_view(request):
    return render(request, 'dsr/dashboard.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')  # Replace 'login' with the name or path to your login page

