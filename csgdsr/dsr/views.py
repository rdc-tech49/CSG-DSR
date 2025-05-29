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


def user_dashboard_view(request):
    return render(request, 'dsr/user/user_dashboard.html')

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


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')  # Replace 'login' with the name or path to your login page


@login_required
def forms_view(request):
    cards = [
        {"title": "CSR", "url_name": "csr_form", "icon": "bi-file-earmark-text", "color": "#0d6efd"},
        {"title": "194 BNSS", "url_name": "194bnss_form", "icon": "bi-clipboard-data", "color": "#6610f2"},
        {"title": "Missing", "url_name": "missing_form", "icon": "bi-person-dash", "color": "#dc3545"},
        {"title": "Maritime Act", "url_name": "maritimeact_form", "icon": "bi-globe", "color": "#20c997"},
        {"title": "Other Cases", "url_name": "othercases_form", "icon": "bi-briefcase", "color": "#6f42c1"},
        {"title": "Rescue", "url_name": "rescue_form", "icon": "bi-life-preserver", "color": "#fd7e14"},
        {"title": "Seizure", "url_name": "seizure_form", "icon": "bi-shield-check", "color": "#198754"},
        {"title": "Forecast", "url_name": "forecast_form", "icon": "bi-cloud-sun", "color": "#0dcaf0"},
        {"title": "Attack on TN Fishermen", "url_name": "fishermen_attack_form", "icon": "bi-person-x", "color": "#ffc107"},
        {"title": "TN Fishermen Arrest", "url_name": "fishermen_arrest_form", "icon": "bi-handcuffs", "color": "#dc3545"},
        {"title": "Vehicle & Boat Status", "url_name": "boat_vehicle_status_form", "icon": "bi-truck", "color": "#6c757d"},
        {"title": "VVC", "url_name": "vvc_form", "icon": "bi-folder2-open", "color": "#20c997"},
        {"title": "Beat", "url_name": "beat_form", "icon": "bi-compass", "color": "#0d6efd"},
        {"title": "Proforma", "url_name": "proforma_form", "icon": "bi-ui-checks", "color": "#198754"},
        {"title": "Boat Patrol", "url_name": "boat_patrol_form", "icon": "bi-ship", "color": "#0dcaf0"},
        {"title": "Vehicle Check", "url_name": "vehicle_check_form", "icon": "bi-search", "color": "#6f42c1"},
    ]
    return render(request, 'dsr/user/forms_page.html', {'cards': cards})





@login_required
def csr_form_view(request):
    return render(request, 'dsr/user/forms/csr_form.html')

@login_required
def bnss194_form_view(request):
    return render(request, 'dsr/user/forms/bnss194_form.html')

@login_required
def missing_form_view(request):
    return render(request, 'dsr/user/forms/missing_form.html')

@login_required
def maritimeact_form_view(request):
    return render(request, 'dsr/user/forms/maritimeact_form.html')

@login_required
def othercases_form(request):
    return render(request, 'dsr/user/forms/othercases_form.html')

@login_required
def rescue_form_view(request):
    return render(request, 'dsr/user/forms/rescue_form.html')

@login_required
def seizure_form_view(request):
    return render(request, 'dsr/user/forms/seizure_form.html')

@login_required
def forecast_form_view(request):
    return render(request, 'dsr/user/forms/forecast_form.html')

@login_required
def fishermen_attack_form_view(request):
    return render(request, 'dsr/user/forms/fishermen_attack_form.html')

@login_required
def fishermen_arrest_form_view(request):
    return render(request, 'dsr/user/forms/fishermen_arrest_form.html')

@login_required
def boat_vehicle_status_form_view(request):
    return render(request, 'dsr/user/forms/boat_vehicle_status_form.html')

@login_required
def vvc_form_view(request):
    return render(request, 'dsr/user/forms/vvc_form.html')

@login_required
def beat_form_view(request):
    return render(request, 'dsr/user/forms/beat_form.html')

@login_required
def proforma_form_view(request):
    return render(request, 'dsr/user/forms/proforma_form.html')

@login_required
def boat_patrol_form_view(request):
    return render(request, 'dsr/user/forms/boat_patrol_form.html')

@login_required
def vehicle_check_form_view(request):
    return render(request, 'dsr/user/forms/vehicle_check_form.html')

#submitted forms summary views
@login_required
def cases_registered_summary_view(request):
    return render(request, 'dsr/user/submitted_forms/cases_registered_summary.html')

@login_required
def rescue_seizure_summary_view(request):
    return render(request, 'dsr/user/submitted_forms/rescue_seizure_summary.html')

@login_required
def forecast_summary_view(request):
    return render(request, 'dsr/user/submitted_forms/forecast_summary.html')

@login_required
def fishermen_attack_arrest_summary_view(request):
    return render(request, 'dsr/user/submitted_forms/fishermen_attack_arrest_summary.html')

@login_required
def vehicle_status_summary_view(request):
    return render(request, 'dsr/user/submitted_forms/vehicle_status_summary.html')

@login_required
def vvc_beat_proforma_summary_view(request):
    return render(request, 'dsr/user/submitted_forms/vvc_beat_proforma_summary.html')

@login_required
def patrol_vehicle_check_summary_view(request):
    return render(request, 'dsr/user/submitted_forms/patrol_vehicle_check_summary.html')

