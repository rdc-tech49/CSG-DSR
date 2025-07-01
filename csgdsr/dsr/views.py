from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from docx import Document
from docx.shared import Inches
from django import forms
from .models import CheckPost, CSR, BNSSMissingCase, OtherCases,Other_Agencies, MaritimeAct, Officer, MPS, CheckPost,Other_Agencies, AttackOnTNFishermen_Choices, ArrestOfTNFishermen_Choices, ArrestOfSLFishermen_Choices, SeizedItemCategory, CustomUser, SeizedItemCategory, PS

from .forms import CustomSignupForm, UpdateUserForm,OfficerForm, CheckPostForm, CSRForm, BNSSMissingCaseForm,othercasesForm, MaritimeActForm,Other_AgenciesForm,OfficerForm, MPSForm, CheckPostForm,Other_AgenciesForm, AttackOnTNFishermen_ChoicesForm,ArrestOfTNFishermen_ChoicesForm, ArrestOfSLFishermen_ChoicesForm, SeizedItemCategoryForm,PSForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Q

from django.template.loader import render_to_string

#home page
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
            if user.is_superuser:
                return redirect('admin_dashboard')  # URL name for admin dashboard
            else:
                return redirect('user_dashboard')

        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'dsr/home.html')

# admin views
@login_required
def admin_dashboard_view(request):
    return render(request, 'dsr/admin/admin_dashboard.html')

@login_required
def admin_users_view(request, user_id=None):
    users = CustomUser.objects.all().order_by('username')
    user_instance = get_object_or_404(CustomUser, id=user_id) if user_id else None

    if request.method == 'POST':
        form = CustomSignupForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            if user_instance:
                messages.success(request, "User updated successfully.")
            else:
                messages.success(request, "User created successfully.")
            return redirect('admin_users_page')
        else:
            messages.error(request, "Please correct the form errors.")
    else:
        form = CustomSignupForm(instance=user_instance)

    context = {
        'form': form,
        'users': users,
        'edit_mode': user_instance is not None,
        'user_id': user_instance.id if user_instance else '',
    }
    return render(request, 'dsr/admin/add_edituser.html', context)

@login_required
def admin_officers_strength_view(request, officer_id=None):
    officers = Officer.objects.all().order_by('rank')
    if officer_id:
        officer_instance = get_object_or_404(Officer, id=officer_id)
    else:
        officer_instance = None

    if request.method == 'POST':
        if officer_instance:
            form = OfficerForm(request.POST, instance=officer_instance)
            if form.is_valid():
                form.save()
                messages.success(request, "Officer details updated successfully!")
                return redirect('admin_officers_strength_page')
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = OfficerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Officer added successfully!")
                return redirect('admin_officers_strength_page')
            else:
                messages.error(request, "Please correct the errors below.")
    else:
        form = OfficerForm(instance=officer_instance)

    context = {
        'form': form,
        'officers': officers,
        'edit_mode': officer_instance is not None,
        'officer_id': officer_instance.id if officer_instance else '',
    }
    return render(request, 'dsr/admin/officers_details.html', context)

@login_required
def admin_MPS_buildings_view(request, mps_id=None, checkpost_id=None,ps_id=None):
    mps_list = MPS.objects.all().order_by('name')
    checkpost_list = CheckPost.objects.all().order_by('name')
    ps_list = PS.objects.all().order_by('name')

    mps_instance = get_object_or_404(MPS, id=mps_id) if mps_id else None
    checkpost_instance = get_object_or_404(CheckPost, id=checkpost_id) if checkpost_id else None
    ps_instance = get_object_or_404(PS, id=ps_id) if ps_id else None
    if request.method == 'POST':
        
        # Handle MPS Form
        if 'mps_submit' in request.POST:
            mps_form = MPSForm(request.POST, instance=mps_instance)
            if mps_form.is_valid():
                mps_form.save()
                if mps_instance:
                    messages.success(request, "MPS updated successfully.")
                else:
                    messages.success(request, "MPS added successfully.")
                return redirect('admin_MPS_buildings_page')
            else:
                messages.error(request, "Please correct the MPS form errors.")
            checkpost_form = CheckPostForm()  # Empty Checkpost form

        # Handle CheckPost Form
        elif 'checkpost_submit' in request.POST:
            checkpost_form = CheckPostForm(request.POST, instance=checkpost_instance)
            if checkpost_form.is_valid():
                checkpost_form.save()
                if checkpost_instance:
                    messages.success(request, "Checkpost updated successfully.")
                else:
                    messages.success(request, "Checkpost added successfully.")
                return redirect('admin_MPS_buildings_page')
            else:
                messages.error(request, "Please correct the Checkpost form errors.")
            mps_form = MPSForm()  # Empty MPS form
        # Handle PS Form
        elif 'ps_submit' in request.POST:
            ps_form = PSForm(request.POST, instance=ps_instance)
            if ps_form.is_valid():
                ps_form.save()
                if ps_instance:
                    messages.success(request, "PS updated successfully.")
                else:
                    messages.success(request, "PS added successfully.")
                return redirect('admin_MPS_buildings_page')
            else:
                messages.error(request, "Please correct the PS form errors.")
            mps_form = MPSForm()

    else:
        mps_form = MPSForm(instance=mps_instance)
        checkpost_form = CheckPostForm(instance=checkpost_instance)
        ps_form = PSForm(instance=ps_instance)
    context = {
        'mps_form': mps_form,
        'checkpost_form': checkpost_form,
        'ps_form': ps_form,
        'mps_list': mps_list,
        'checkpost_list': checkpost_list,
        'ps_list': ps_list,
        'edit_mps': mps_instance is not None,
        'edit_checkpost': checkpost_instance is not None,
        'edit_ps': ps_instance is not None,
        'mps_id': mps_instance.id if mps_instance else '',
        'checkpost_id': checkpost_instance.id if checkpost_instance else '',
        'ps_id': ps_instance.id if ps_instance else '',
    }
    return render(request, 'dsr/admin/buildings.html', context)

@login_required
def admin_other_agencies_view(request, agency_id=None, attacker_id=None, arrest_tn_id=None, arrest_sl_id=None):
    
    agencies = Other_Agencies.objects.all().order_by('agency_name')
    # attackers = AttackOnTNFishermen_Choices.objects.all().order_by('attacker_name')
    # arrest_tn = ArrestOfTNFishermen_Choices.objects.all().order_by('arrested_by')
    # arrest_sl = ArrestOfSLFishermen_Choices.objects.all().order_by('arrested_by')

    agency_instance = get_object_or_404(Other_Agencies, id=agency_id) if agency_id else None
    # attacker_instance = get_object_or_404(AttackOnTNFishermen_Choices, id=attacker_id) if attacker_id else None
    # arrest_tn_instance = get_object_or_404(ArrestOfTNFishermen_Choices, id=arrest_tn_id) if arrest_tn_id else None
    # arrest_sl_instance = get_object_or_404(ArrestOfSLFishermen_Choices, id=arrest_sl_id) if arrest_sl_id else None

    if request.method == 'POST':
        
        # Other Agencies
        if 'agency_submit' in request.POST:
            form = Other_AgenciesForm(request.POST, instance=agency_instance)
            if form.is_valid():
                form.save()
                messages.success(request, "Other Agency saved successfully.")
                return redirect('admin_other_agencies_page')
            else:
                messages.error(request, "Please correct the errors in Other Agency form.")
            attacker_form = AttackOnTNFishermen_ChoicesForm()
            arrest_tn_form = ArrestOfTNFishermen_ChoicesForm()
            arrest_sl_form = ArrestOfSLFishermen_ChoicesForm()

        # Attack on TN Fishermen
        # elif 'attacker_submit' in request.POST:
        #     attacker_form = AttackOnTNFishermen_ChoicesForm(request.POST, instance=attacker_instance)
        #     if attacker_form.is_valid():
        #         attacker_form.save()
        #         messages.success(request, "Attacker name saved successfully.")
        #         return redirect('admin_other_agencies_page')
        #     else:
        #         messages.error(request, "Please correct the errors in Attacker form.")
        #     form = Other_AgenciesForm()
        #     arrest_tn_form = ArrestOfTNFishermen_ChoicesForm()
        #     arrest_sl_form = ArrestOfSLFishermen_ChoicesForm()

        # # Arrest of TN Fishermen
        # elif 'arrest_tn_submit' in request.POST:
        #     arrest_tn_form = ArrestOfTNFishermen_ChoicesForm(request.POST, instance=arrest_tn_instance)
        #     if arrest_tn_form.is_valid():
        #         arrest_tn_form.save()
        #         messages.success(request, "Arresting Authority (TN) saved successfully.")
        #         return redirect('admin_other_agencies_page')
        #     else:
        #         messages.error(request, "Please correct the errors in Arresting Authority (TN) form.")
        #     form = Other_AgenciesForm()
        #     attacker_form = AttackOnTNFishermen_ChoicesForm()
        #     arrest_sl_form = ArrestOfSLFishermen_ChoicesForm()

        # # Arrest of SL Fishermen
        # elif 'arrest_sl_submit' in request.POST:
        #     arrest_sl_form = ArrestOfSLFishermen_ChoicesForm(request.POST, instance=arrest_sl_instance)
        #     if arrest_sl_form.is_valid():
        #         arrest_sl_form.save()
        #         messages.success(request, "Arresting Authority (SL) saved successfully.")
        #         return redirect('admin_other_agencies_page')
        #     else:
        #         messages.error(request, "Please correct the errors in Arresting Authority (SL) form.")
        #     form = Other_AgenciesForm()
        #     attacker_form = AttackOnTNFishermen_ChoicesForm()
        #     arrest_tn_form = ArrestOfTNFishermen_ChoicesForm()

    else:
        form = Other_AgenciesForm(instance=agency_instance)
        # attacker_form = AttackOnTNFishermen_ChoicesForm(instance=attacker_instance)
        # arrest_tn_form = ArrestOfTNFishermen_ChoicesForm(instance=arrest_tn_instance)
        # arrest_sl_form = ArrestOfSLFishermen_ChoicesForm(instance=arrest_sl_instance)

    context = {
        'form': form,
        # 'attacker_form': attacker_form,
        # 'arrest_tn_form': arrest_tn_form,
        # 'arrest_sl_form': arrest_sl_form,
        'agencies': agencies,
        # 'attackers': attackers,
        # 'arrest_tn': arrest_tn,
        # 'arrest_sl': arrest_sl,
        'edit_agency': agency_instance is not None,
        # 'edit_attacker': attacker_instance is not None,
        # 'edit_arrest_tn': arrest_tn_instance is not None,
        # 'edit_arrest_sl': arrest_sl_instance is not None,
        'agency_id': agency_instance.id if agency_instance else '',
        # 'attacker_id': attacker_instance.id if attacker_instance else '',
        # 'arrest_tn_id': arrest_tn_instance.id if arrest_tn_instance else '',
        # 'arrest_sl_id': arrest_sl_instance.id if arrest_sl_instance else '',
    }
    return render(request, 'dsr/admin/other_agencies.html', context)

@login_required
def admin_seizure_items_view(request, item_id=None):
    items = SeizedItemCategory.objects.all().order_by('item_name')
    item_instance = get_object_or_404(SeizedItemCategory, id=item_id) if item_id else None

    if request.method == 'POST':
        form = SeizedItemCategoryForm(request.POST, instance=item_instance)
        if form.is_valid():
            form.save()
            if item_instance:
                messages.success(request, "Seized Item updated successfully.")
            else:
                messages.success(request, "Seized Item added successfully.")
            return redirect('admin_seizure_items_page')
        else:
            messages.error(request, "Please correct the form errors.")
    else:
        form = SeizedItemCategoryForm(instance=item_instance)

    context = {
        'form': form,
        'items': items,
        'edit_mode': item_instance is not None,
        'item_id': item_instance.id if item_instance else '',
    }
    return render(request, 'dsr/admin/seizure_items.html', context)

#add add checkppost view
@login_required
def add_checkpost(request):
    if request.method == 'POST':
        form = CheckPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New checkpost added successfully!")
            return redirect('add_checkpost')  # redirect to the same form or elsewhere
    else:
        form = CheckPostForm()
    
    return render(request, 'dsr/admin.add_checkpost.html', {'form': form})

#Other_AgenciesForm view
@login_required
def other_agencies_form_view(request):
    if request.method == 'POST':
        form = Other_AgenciesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Other agency added successfully!")
            return redirect('other_agencies_form')
    else:
        form = Other_AgenciesForm()
    return render(request, 'dsr/admin.other_agencies_form.html', {'form': form})

def arrest_of_sl_fishermen_choices_form_view(request):
    return HttpResponse("<h2>Arrest of SL Fishermen - Form: No page created yet.</h2>")

def officer_form_view(request):
    return HttpResponse("<h2>Arrest of SL Fishermen - Form: No page created yet.</h2>")

def seized_item_category_form_view(request):
    return HttpResponse("<h2>Seized Item Category - Form: No page created yet.</h2>")

def attack_on_tnfishermen_choices_form_view(request):
    return HttpResponse("<h2>Attack on TN Fishermen - Form: No page created yet.</h2>")

def tnfishermen_arrest_choices_form_view(request):
    return HttpResponse("<h2>TN Fishermen Arrest - Form: No page created yet.</h2>")

def arrest_of_sl_fishermen_choices_form_view(request):
    return HttpResponse("<h2>Arrest of SL Fishermen - Form: No page created yet.</h2>")

def rescue_at_beach_form_view(request):
    return HttpResponse("<h2>Rescue at Beach - Form: No page created yet.</h2>")

def rescue_at_sea_form_view(request):
    return HttpResponse("<h2>Rescue at Sea - Form: No page created yet.</h2>")

def attack_on_tnfishermen_view(request):
    return HttpResponse("<h2>Attack on TN Fishermen - Form: No page created yet.</h2>")

def tnfishermen_arrest_form_view(request):  
    return HttpResponse("<h2>TN Fishermen Arrest - Form: No page created yet.</h2>")

def arrest_of_sl_fishermen_form_view(request):
    return HttpResponse("<h2>Arrest of SL Fishermen - Form: No page created yet.</h2>")

def onroad_vehicle_status_form_view(request):   
    return HttpResponse("<h2>On Road Vehicle Status - Form: No page created yet.</h2>")

def onwater_vehicle_status_form_view(request):
    return HttpResponse("<h2>On Water Vehicle Status - Form: No page created yet.</h2>")

def vvc_meeting_form_view(request): 
    return HttpResponse("<h2>VVC Meeting - Form: No page created yet.</h2>")

def beat_details_form_view(request):    
    return HttpResponse("<h2>Beat Details - Form: No page created yet.</h2>")

def atv_patrol_form_view(request):
    return HttpResponse("<h2>ATV Patrol - Form: No page created yet.</h2>")

def vehicle_checkpost_form_view(request):
    return HttpResponse("<h2>Vehicle Checkpost - Form: No page created yet.</h2>")

def vehicle_check_others_form_view(request):
    return HttpResponse("<h2>Vehicle Check Others - Form: No page created yet.</h2>")







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

# users 
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
    cards = [
        {"title": "CSR", "url_name": "csr_form", "icon": "bi-file-earmark-text", "color": "#0d6efd"},
        {"title": "194 BNSS", "url_name": "bnss_missing_form", "icon": "bi-clipboard-data", "color": "#6610f2"},
        {"title": "Missing", "url_name": "bnss_missing_form", "icon": "bi-person-dash", "color": "#dc3545"},
        {"title": "Maritime Act", "url_name": "maritimeact_form", "icon": "bi-globe", "color": "#20c997"},
        {"title": "Other Cases", "url_name": "othercases_form", "icon": "bi-briefcase", "color": "#6f42c1"},
        {"title": "Rescue", "url_name": "rescue_at_beach_form", "icon": "bi-life-preserver", "color": "#fd7e14"},
        {"title": "Seizure", "url_name": "seizure_form", "icon": "bi-shield-check", "color": "#198754"},
        {"title": "Forecast", "url_name": "forecast_form", "icon": "bi-cloud-sun", "color": "#0dcaf0"},
        {"title": "Attack on TN Fishermen", "url_name": "attack_on_tnfishermen_form", "icon": "bi-person-x", "color": "#ffc107"},
        {"title": "TN Fishermen Arrest", "url_name": "tnfishermen_arrest_form", "icon": "bi-handcuffs", "color": "#dc3545"},
        {"title": "Vehicle & Boat Status", "url_name": "onwater_vehicle_status_form", "icon": "bi-truck", "color": "#6c757d"},
        {"title": "VVC", "url_name": "vvc_meeting_form", "icon": "bi-folder2-open", "color": "#20c997"},
        {"title": "Beat", "url_name": "beat_details_form", "icon": "bi-compass", "color": "#0d6efd"},
        {"title": "Proforma", "url_name": "proforma_form", "icon": "bi-ui-checks", "color": "#198754"},
        {"title": "Boat Patrol", "url_name": "boat_patrol_form", "icon": "bi-ship", "color": "#0dcaf0"},
        {"title": "Vehicle Check", "url_name": "vehicle_checkpost_form", "icon": "bi-search", "color": "#6f42c1"},
    ]
    return render(request, 'dsr/user/forms_page.html', {'cards': cards})

@login_required
def csr_form_view(request):
    if request.method == 'POST':
        form = CSRForm(request.POST)
        if form.is_valid():
            csr = form.save(commit=False)
            csr.user = request.user  # ✅ Assign the logged-in user
            csr.save()
            messages.success(request, 'CSR form submitted successfully!')
            return redirect('cases_summary')
    else:
        form = CSRForm()
    return render(request, 'dsr/user/forms/csr_form.html', {'form': form})

@login_required
def bnss_missing_form_view(request):
    if request.method == 'POST':
        form = BNSSMissingCaseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            # instance.date_submitted = timezone.now()
            instance.save()
            messages.success(request, "Form submitted successfully!")
            return redirect('cases_summary')  # or wherever you want to go
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BNSSMissingCaseForm()

    return render(request, 'dsr/user/forms/194bnss_missing_form.html', {'form': form})

@login_required
def othercases_form(request):
    if request.method == 'POST':
        form = othercasesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Form submitted successfully!")
            return redirect('cases_summary')  # or wherever you want to go
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = othercasesForm()

    return render(request, 'dsr/user/forms/othercases_form.html',{'form': form})

@login_required
def maritimeact_form_view(request):
    if request.method == 'POST':
        form = MaritimeActForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Maritime Act form submitted successfully!")
            return redirect('cases_summary')
    else:
        form = MaritimeActForm()
    
    return render(request, 'dsr/user/forms/maritimeact_form.html', {'form': form})



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
    csr_list = CSR.objects.filter(user=request.user).order_by('-date_of_receipt')
    bnss_cases = BNSSMissingCase.objects.filter(user=request.user, case_category='194 BNSS').order_by('-date_of_receipt')
    missing_cases = BNSSMissingCase.objects.filter(user=request.user, case_category='Missing').order_by('-date_of_receipt')
    other_cases = OtherCases.objects.filter(user=request.user).order_by('-date_of_receipt')
    maritime_cases= MaritimeAct.objects.filter(user=request.user).order_by('-date_of_receipt')
    
    return render(request, 'dsr/user/submitted_forms/cases_registered_summary.html', {
        'csr_list': csr_list,
        'bnss_cases': bnss_cases,
        'missing_cases': missing_cases,
        'other_cases': other_cases,
        'maritime_cases': maritime_cases,

    })

#search for csr
@login_required
def csr_ajax_search_view(request):
    query = request.GET.get('q', '').strip()
    csr_list = CSR.objects.all()

    if query:
        csr_list = csr_list.filter(
            Q(csr_number__icontains=query) |
            Q(petitioner__icontains=query) |
            Q(io_icontains=query) 
        )

    data = [
        {
            'id': csr.id,
            'csr_number': csr.csr_number,
            'date_of_receipt': csr.date_of_receipt.strftime('%Y-%m-%d'),
            'petitioner': csr.petitioner,
            'io': csr.io,
        }
        for csr in csr_list
    ]
    return JsonResponse(data, safe=False)

#bnss search
@login_required
def bnss194_cases_ajax_search_view(request):
    query = request.GET.get('q', '').strip()
    cases = BNSSMissingCase.objects.filter(case_category='194 BNSS', user=request.user)

    if query:
        cases = cases.filter(
            Q(crime_number__icontains=query) |
            Q(date_of_occurrence__icontains=query) |
            Q(date_of_receipt__icontains=query) |
            Q(ps_limit__icontains=query) |
            Q(io__icontains=query) |
            Q(transfered_to__icontains=query)
        )

    data = [
        {
            'id': case.id,
            'crime_number': case.crime_number,
            'date_of_occurrence': case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs'),
            'date_of_receipt': case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs'),
            'ps_limit': case.ps_limit,
            'io': case.io,
            'transfered_to': case.transfered_to,
        }
        for case in cases
    ]
    return JsonResponse(data, safe=False)

#search for missing cases
@login_required
def missing_ajax_search_view(request):
    query = request.GET.get('q', '').strip()
    cases = BNSSMissingCase.objects.filter(case_category='Missing', user=request.user)

    if query:
        cases = cases.filter(
            Q(crime_number__icontains=query) |
            Q(date_of_occurrence__icontains=query) |
            Q(date_of_receipt__icontains=query) |
            Q(ps_limit__icontains=query) |
            Q(io__icontains=query) |
            Q(transfered_to__icontains=query)
        )

    data = [
        {
            'id': case.id,
            'crime_number': case.crime_number,
            'date_of_occurrence': case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs'),
            'date_of_receipt': case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs'),
            'ps_limit': case.ps_limit,
            'io': case.io,
            'transfered_to': case.transfered_to,
        }
        for case in cases
    ]
    return JsonResponse(data, safe=False)

#search for other cases
@login_required
def othercases_ajax_search_view(request):
    query = request.GET.get('q', '').strip()
    cases = OtherCases.objects.filter(user=request.user)

    if query:
        cases = cases.filter(
            Q(crime_number__icontains=query) |
            Q(date_of_occurrence__icontains=query) |
            Q(date_of_receipt__icontains=query) |
            Q(ps_limit__icontains=query) |
            Q(io__icontains=query) |
            Q(transfered_to__icontains=query)
        )

    data = [
        {
            'id': case.id,
            'crime_number': case.crime_number,
            'date_of_occurrence': case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs'),
            'date_of_receipt': case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs'),
            'ps_limit': case.ps_limit,
            'io': case.io,
            'transfered_to': case.transfered_to,
        }
        for case in cases
    ]
    return JsonResponse(data, safe=False)

#search for maritime act cases
@login_required
def maritimeact_ajax_search_view(request):
    query = request.GET.get('q', '').strip()
    cases = MaritimeAct.objects.filter(user=request.user)

    if query:
        cases = cases.filter(
            Q(crime_number__icontains=query) |
            Q(date_of_occurrence__icontains=query) |
            Q(date_of_receipt__icontains=query) |
            Q(ps_limit__icontains=query) |
            Q(io__icontains=query) |
            Q(transfered_to__icontains=query)
            
        )

    data = [
        {
            'id': case.id,
            'crime_number': case.crime_number,
            'date_of_occurrence': case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs'),
            'date_of_receipt': case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs'),
            'ps_limit': case.ps_limit,
            'io': case.io,
            'transfered_to': case.transfered_to,
        }
        for case in cases
    ]
    return JsonResponse(data, safe=False)

#exprt CSR to Word document
@login_required
def csr_export_word_view(request):
    csrs = CSR.objects.all().order_by('date_of_receipt')
    doc = Document()

    for csr in csrs:
        table = doc.add_table(rows=0, cols=2)
        table.style = 'Table Grid'

        # Fields to include in the Word document
        fields = [
            ("CSR No.", csr.csr_number),
            ("MPS Limit ", csr.mps_limit),  # Directly use it as string
            ("Date of Receipt", csr.date_of_receipt.strftime('%Y-%m-%d') if csr.date_of_receipt else ''),
            ("Place of Occurrence", csr.place_of_occurrence),
            ("Petitioner", csr.petitioner),
            ("Counter Petitioner", csr.counter_petitioner),
            ("Nature of Petition", csr.nature_of_petition),
            ("Gist of Petition", csr.gist_of_petition),
            ("IO", csr.io)
        ]

        for label, value in fields:
            row = table.add_row().cells
            row[0].text = label
            row[1].text = str(value)

        doc.add_paragraph()  # Empty line
        doc.add_paragraph()  # Second empty line

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename="CSR_Export.docx"'
    doc.save(response)
    return response

#export 194 BNSS cases to Word document
@login_required
def bnss_194_export_word_view(request):
    bnsss = BNSSMissingCase.objects.filter(case_category='194 BNSS').order_by('date_of_receipt')
    doc = Document()

    for bnss in bnsss:
        table = doc.add_table(rows=0, cols=2)
        table.style = 'Table Grid'

        # Fields to include in the Word document
        fields = [
            ("Crime No.", bnss.crime_number),
            ("Police Station Limit", bnss.ps_limit),  # Directly use it as string
            ("MPS Limit", bnss.mps_limit),
            ("Date of Occurrence", bnss.date_of_occurrence.strftime('%Y-%m-%d %H:%M') if bnss.date_of_occurrence else ''),
            ("Date of Receipt", bnss.date_of_receipt.strftime('%Y-%m-%d') if bnss.date_of_receipt else ''),
            ("Place of Occurrence", bnss.place_of_occurrence),
            ("Petitioner", bnss.petitioner),
            ("Diseased", bnss.diseased if bnss.case_category == '194 BNSS' else ''),
            ("Missing Person", bnss.missing_person if bnss.case_category == 'Missing' else ''),
            ("Gist of Case", bnss.gist_of_case),
            ("IO", bnss.io),
            ("Transfered To", bnss.transfered_to),
            
        ]

        for label, value in fields:
            row = table.add_row().cells
            row[0].text = label
            row[1].text = str(value)

        doc.add_paragraph()  # Empty line
        doc.add_paragraph()  # Second empty line

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename="BNSS194_Export.docx"'
    doc.save(response)
    return response

#export missing cases to Word document
@login_required
def missing_export_word_view(request):
    missings = BNSSMissingCase.objects.filter(case_category='Missing').order_by('date_of_receipt')
    doc = Document()

    for missing in missings:
        table = doc.add_table(rows=0, cols=2)
        table.style = 'Table Grid'

        # Fields to include in the Word document
        fields = [
            ("Crime No.", missing.crime_number),
            ("Police Station Limit", missing.ps_limit),  # Directly use it as string
            ("MPS Limit", missing.mps_limit),
            ("Date of Occurrence", missing.date_of_occurrence.strftime('%Y-%m-%d %H:%M') if missing.date_of_occurrence else ''),
            ("Date of Receipt", missing.date_of_receipt.strftime('%Y-%m-%d') if missing.date_of_receipt else ''),
            ("Place of Occurrence", missing.place_of_occurrence),
            ("Petitioner", missing.petitioner),
            ("Diseased", missing.diseased if missing.case_category == '194 BNSS' else ''),
            ("Missing Person", missing.missing_person if missing.case_category == 'Missing' else ''),
            ("Gist of Case", missing.gist_of_case),
            ("IO", missing.io),
            ("Transfered To", missing.transfered_to),
        ]

        for label, value in fields:
            row = table.add_row().cells
            row[0].text = label
            row[1].text = str(value)

        doc.add_paragraph()  # Empty line
        doc.add_paragraph()  # Second empty line

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename="Missing_Export.docx"'
    doc.save(response)
    return response

#export other cases to Word document
@login_required
def othercases_export_word_view(request):
    other_cases = OtherCases.objects.filter(user=request.user).order_by('date_of_receipt')
    doc = Document()

    for case in other_cases:
        table = doc.add_table(rows=0, cols=2)
        table.style = 'Table Grid'

        # Fields to include in the Word document
        fields = [
            ("Crime No.", case.crime_number),
            ("Police Station Limit", case.ps_limit),  # Directly use it as string
            ("MPS Limit", case.mps_limit),
            ("Date of Occurrence", case.date_of_occurrence.strftime('%Y-%m-%d %H:%M') if case.date_of_occurrence else ''),
            ("Date of Receipt", case.date_of_receipt.strftime('%Y-%m-%d') if case.date_of_receipt else ''),
            ("Place of Occurrence", case.place_of_occurrence),
            ("Petitioner", case.petitioner),
            ("Diseased", case.diseased if case.diseased else ''),
            ("Injured", case.injured if case.injured else ''),
            ("Accused", case.accused if case.accused else ''),
            ("Gist of Case", case.gist_of_case),
            ("IO", case.io),
            ("Transfered To", case.transfered_to),
        ]

        for label, value in fields:
            row = table.add_row().cells
            row[0].text = label
            row[1].text = str(value)

        doc.add_paragraph()
        doc.add_paragraph()  # Second empty line
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename="Other_Cases_Export.docx"'
    doc.save(response)
    return response

#export maritime act cases to Word document
@login_required
def maritimeact_export_word_view(request):
    maritime_cases = MaritimeAct.objects.filter(user=request.user).order_by('date_of_receipt')
    doc = Document()

    for case in maritime_cases:
        table = doc.add_table(rows=0, cols=2)
        table.style = 'Table Grid'

        # Fields to include in the Word document
        fields = [
            ("Crime No.", case.crime_number),
            ("Police Station Limit", case.ps_limit),  # Directly use it as string
            ("MPS Limit", case.mps_limit),
            ("Date of Occurrence", case.date_of_occurrence.strftime('%Y-%m-%d %H:%M') if case.date_of_occurrence else ''),
            ("Date of Receipt", case.date_of_receipt.strftime('%Y-%m-%d') if case.date_of_receipt else ''),
            ("Place of Occurrence", case.place_of_occurrence),
            ("Petitioner", case.petitioner),
            ("Accused", case.accused if case.accused else ''),
            ("Gist of Case", case.gist_of_case),
            ("IO", case.io),
            ("Transfered To", case.transfered_to)
        ]

        for label, value in fields:
            row = table.add_row().cells
            row[0].text = label
            row[1].text = str(value)

        doc.add_paragraph()
        doc.add_paragraph()  # Second empty line
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename="Maritime_Cases_Export.docx"'
    doc.save(response)
    return response


#export individual CSR
@login_required
def csr_download_view(request, pk):
    csr = get_object_or_404(CSR, pk=pk)

    # Create a new Word document
    doc = Document()
    doc.add_heading('Community Service Register (CSR)', level=1)

    # Create a table with 2 columns
    table = doc.add_table(rows=0, cols=2)
    table.style = 'Table Grid'

    # Helper function to add a row
    def add_row(field, value):
        row = table.add_row().cells
        row[0].text = field
        row[1].text = str(value) if value else ''

    # Add CSR details to the table
    add_row('CSR Number', csr.csr_number)
    add_row('MPS Limit ', str(csr.mps_limit))
    add_row('Date of Receipt', csr.date_of_receipt.strftime('%Y-%m-%d'))
    add_row('Place of Occurrence', csr.place_of_occurrence)
    add_row('Petitioner', csr.petitioner)
    add_row('Counter Petitioner', csr.counter_petitioner)
    add_row('Nature of Petition', csr.nature_of_petition)
    add_row('Gist of Petition', csr.gist_of_petition)
    add_row('IO', csr.io)

    # Prepare HTTP response with docx content
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename=CSR_{csr.csr_number}.docx'

    doc.save(response)
    return response

#export individual BNSS194 case
@login_required
def bnss194_download_view(request, pk):
    case = get_object_or_404(BNSSMissingCase, pk=pk)

    doc = Document()
    doc.add_heading(f"{case.case_category} Case Details", level=1)

    # Create table with two columns
    table = doc.add_table(rows=0, cols=2)
    table.style = 'Table Grid'

    def add_row(label, value):
        row = table.add_row().cells
        row[0].text = str(label)
        row[1].text = str(value) if value else ''

    # Add data
    add_row('Crime Number', case.crime_number)
    add_row('Case Category', case.case_category)
    add_row('Police Station Limit', case.ps_limit)
    add_row('MPS Limit', case.mps_limit)
    add_row('Date of Occurrence', case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_occurrence else '')
    add_row('Date of Receipt', case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_receipt else '')
    add_row('Place of Occurrence', case.place_of_occurrence)
    if case.case_category == '194 BNSS':
        add_row('Diseased', case.diseased)
    elif case.case_category == 'Missing':
        add_row('Missing Person', case.missing_person)
    add_row('Petitioner', case.petitioner)
    add_row('Gist of Case', case.gist_of_case)
    add_row('IO', case.io)
    add_row('Transfered To', case.transfered_to)

    # Prepare response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    filename = f"{case.case_category.replace(' ', '_')}_{case.crime_number}.docx"
    response['Content-Disposition'] = f'attachment; filename={filename}'
    doc.save(response)
    return response

#export individual missing case
@login_required
def othercases_download_view(request, pk):
    case = get_object_or_404(OtherCases, pk=pk, user=request.user)

    doc = Document()
    doc.add_heading('Other Cases Details', level=1)

    # Create table with two columns
    table = doc.add_table(rows=0, cols=2)
    table.style = 'Table Grid'

    def add_row(label, value):
        row = table.add_row().cells
        row[0].text = str(label)
        row[1].text = str(value) if value else ''

    # Add data
    add_row('Crime Number', case.crime_number)
    add_row('Police Station Limit', case.ps_limit)
    add_row('MPS Limit', case.mps_limit)
    add_row('Date of Occurrence', case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_occurrence else '')
    add_row('Date of Receipt', case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_receipt else '')
    add_row('Place of Occurrence', case.place_of_occurrence)
    add_row('Petitioner', case.petitioner)
    add_row('Diseased', case.diseased if case.diseased else '')
    add_row('Injured', case.injured if case.injured else '')
    add_row('Accused', case.accused if case.accused else '')
    add_row('Gist of Case', case.gist_of_case)
    add_row('IO', case.io)
    add_row('Transfered To', case.transfered_to)

    # Prepare response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    filename = f"Other_Case_{case.crime_number}.docx"
    response['Content-Disposition'] = f'attachment; filename={filename}'
    doc.save(response)
    return response

#export individual maritime act case
@login_required
def maritimeact_download_view(request, pk):
    case = get_object_or_404(MaritimeAct, pk=pk, user=request.user)

    doc = Document()
    doc.add_heading('Maritime Act Case Details', level=1)

    # Create table with two columns
    table = doc.add_table(rows=0, cols=2)
    table.style = 'Table Grid'

    def add_row(label, value):
        row = table.add_row().cells
        row[0].text = str(label)
        row[1].text = str(value) if value else ''

    # Add data
    add_row('Crime Number', case.crime_number)
    add_row('Police Station Limit', case.ps_limit)
    add_row('MPS Limit', case.mps_limit)
    add_row('Date of Occurrence', case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_occurrence else '')
    add_row('Date of Receipt', case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_receipt else '')
    add_row('Place of Occurrence', case.place_of_occurrence)
    add_row('Petitioner', case.petitioner)
    add_row('Accused', case.accused if case.accused else '')
    add_row('Gist of Case', case.gist_of_case)
    add_row('IO', case.io)
    add_row('Transfered To', case.transfered_to)

    # Prepare response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    filename = f"Maritime_Case_{case.crime_number}.docx"
    response['Content-Disposition'] = f'attachment; filename={filename}'
    doc.save(response)
    return response

# CSR edit view
@login_required
def csr_edit_view(request, pk):
    csr = get_object_or_404(CSR, pk=pk)
    if request.method == 'POST':
        form = CSRForm(request.POST, instance=csr)
        if form.is_valid():
            form.save()
            messages.success(request, 'CSR updated successfully!')
            return redirect('cases_summary')
    else:
        form = CSRForm(instance=csr)

    return render(request, 'dsr/user/forms/csr_form.html', {'form': form, 'edit_mode': True}) 

# BNSS194 edit view
@login_required
def bnss_missing_edit_view(request, pk):
    case = get_object_or_404(BNSSMissingCase, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BNSSMissingCaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('cases_summary')
    else:
        form = BNSSMissingCaseForm(instance=case)
    return render(request, 'dsr/user/forms/194bnss_missing_form.html', {'form': form, 'edit_mode': True})

# Other cases edit view
@login_required
def othercases_edit_view(request, pk):
    case = get_object_or_404(OtherCases, pk=pk, user=request.user)
    if request.method == 'POST':
        form = othercasesForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            messages.success(request, 'Other case updated successfully!')
            return redirect('cases_summary')
    else:
        form = othercasesForm(instance=case)

    return render(request, 'dsr/user/forms/othercases_form.html', {'form': form, 'edit_mode': True})

# Maritime Act edit view
@login_required
def maritimeact_edit_view(request, pk):
    case = get_object_or_404(MaritimeAct, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MaritimeActForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            messages.success(request, 'Maritime Act case updated successfully!')
            return redirect('cases_summary')
    else:
        form = MaritimeActForm(instance=case)

    return render(request, 'dsr/user/forms/maritimeact_form.html', {'form': form, 'edit_mode': True})

#CSR delete view
@login_required
def csr_delete_view(request, pk):
    csr = get_object_or_404(CSR, pk=pk)
    csr.delete()
    messages.success(request, 'CSR entry deleted successfully!')
    return redirect('cases_summary')  # Adjust this to your summary view name

# BNSS194 delete view
@login_required
def bnss_missing_delete_view(request, pk):
    case = get_object_or_404(BNSSMissingCase, pk=pk, user=request.user)
    case.delete()
    return redirect('cases_summary')

# Other cases delete view
@login_required
def othercases_delete_view(request, pk):
    case = get_object_or_404(OtherCases, pk=pk, user=request.user)
    case.delete()
    messages.success(request, 'Other case entry deleted successfully!')
    return redirect('cases_summary')

# Maritime Act delete view
@login_required
def maritimeact_delete_view(request, pk):
    case = get_object_or_404(MaritimeAct, pk=pk, user=request.user)
    case.delete()
    messages.success(request, 'Maritime Act case entry deleted successfully!')
    return redirect('cases_summary')


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

