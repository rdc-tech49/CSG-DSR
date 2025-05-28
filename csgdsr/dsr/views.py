from django.shortcuts import render, redirect
from .forms import CustomSignupForm, UpdateUserForm, CSRForm, FIRForm
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

@login_required
def forms_view(request):
    return render(request, 'dsr/user/forms_page.html')

@login_required
def register_case_form_view(request):
    csr_form = CSRForm()
    fir_form = FIRForm()

    if request.method == 'POST':
        if 'submit_csr' in request.POST:
            csr_form = CSRForm(request.POST)
            if csr_form.is_valid():
                csr_form.save()
                return redirect('register_case_form')
        elif 'submit_fir' in request.POST:
            fir_form = FIRForm(request.POST)
            if fir_form.is_valid():
                fir_form.save()
                return redirect('register_case_form')

    return render(request, 'dsr/user/register_case.html', {
        'csr_form': csr_form,
        'fir_form': fir_form
    })

@login_required
def rescue_seizure_form_view(request):
    return render(request, 'dsr/rescue_seizure.html')

@login_required
def forecast_form_view(request):
    return render(request, 'dsr/forecast.html')

@login_required
def fishermen_attack_arrest_form_view(request):
    return render(request, 'dsr/fishermen_attacks.html')

@login_required
def vehicle_status_form_view(request):
    return render(request, 'dsr/vehicle_status.html')

@login_required
def vvc_beat_proforma_form_view(request):
    return render(request, 'dsr/vvc_beat_proforma.html')

@login_required
def patrol_vehicle_check_form_view(request):
    return render(request, 'dsr/patrol_vehicle_check.html')

@login_required
def vvc_view(request):
    return render(request, 'dsr/vvc.html')

@login_required
def beat_proforma_view(request):
    return render(request, 'dsr/beat_proforma.html')