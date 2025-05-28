from django.shortcuts import render, redirect
from .forms import CustomSignupForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

from .forms import UpdateUserForm
from django import forms
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

# dsr/views.py

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('home')
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

            return redirect('user_dashboard')  # or wherever you want to redirect after login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'dsr/home.html')

def user_dashboard_view(request):
    return render(request, 'dsr/user/user_dashboard.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')  # Replace 'login' with the name or path to your login page

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'dsr/registration/password_change.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Your password is successfully updated.")
        return super().form_valid(form)


@login_required
def update_user_view(request): 
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been updated. Please log in again.")
            logout(request)  # Log the user out after updating
            return redirect('home')  # Replace 'home' with your desired URL name
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'dsr/registration/update_user.html', {'form': form})