from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from docx import Document
from docx.shared import Inches
from django import forms
from .forms import CustomSignupForm, UpdateUserForm,CSRForm, BNSSMissingCaseForm,othercasesForm, MaritimeActForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import CSR, BNSSMissingCase, othercases, maritimeact

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Q

from django.template.loader import render_to_string

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
        {"title": "194 BNSS", "url_name": "bnss_missing_form", "icon": "bi-clipboard-data", "color": "#6610f2"},
        {"title": "Missing", "url_name": "bnss_missing_form", "icon": "bi-person-dash", "color": "#dc3545"},
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
    other_cases = othercases.objects.filter(user=request.user).order_by('-date_of_receipt')
    maritime_cases= maritimeact.objects.filter(user=request.user).order_by('-date_of_receipt')
    
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
            Q(petitioner__icontains=query)
        )

    data = [
        {
            'id': csr.id,
            'csr_number': csr.csr_number,
            'date_of_receipt': csr.date_of_receipt.strftime('%Y-%m-%d'),
            'petitioner': csr.petitioner,
        }
        for csr in csr_list
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
            ("Police Station", csr.police_station),  # Directly use it as string
            ("Date of Receipt", csr.date_of_receipt.strftime('%Y-%m-%d') if csr.date_of_receipt else ''),
            ("Place of Occurrence", csr.place_of_occurrence),
            ("Petitioner", csr.petitioner),
            ("Counter Petitioner", csr.counter_petitioner),
            ("Nature of Petition", csr.nature_of_petition),
            ("Gist of Petition", csr.gist_of_petition),
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
    add_row('Police Station', str(csr.police_station))
    add_row('Date of Receipt', csr.date_of_receipt.strftime('%Y-%m-%d'))
    add_row('Petitioner', csr.petitioner)
    add_row('Counter Petitioner', csr.counter_petitioner)
    add_row('Nature of Petition', csr.nature_of_petition)
    add_row('Gist of Petition', csr.gist_of_petition)

    # Prepare HTTP response with docx content
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename=CSR_{csr.csr_number}.docx'

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

#CSR delete view
@login_required
def csr_delete_view(request, pk):
    csr = get_object_or_404(CSR, pk=pk)
    csr.delete()
    messages.success(request, 'CSR entry deleted successfully!')
    return redirect('cases_summary')  # Adjust this to your summary view name


@login_required
def bnss194_cases_ajax_search_view(request):
    query = request.GET.get('q', '').strip()
    cases = BNSSMissingCase.objects.filter(case_category='194 BNSS', user=request.user)

    if query:
        cases = cases.filter(
            Q(crime_number__icontains=query) |
            Q(petitioner__icontains=query) |
            Q(police_station__icontains=query) |
            Q(date_of_occurrence__icontains=query) |
            Q(date_of_receipt__icontains=query)
        )

    data = [
        {
            'id': case.id,
            'crime_number': case.crime_number,
            'date_of_receipt': case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs'),
            'date_of_occurrence': case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs'),
            'police_station': case.police_station,
            'mps_limit': case.mps_limit,
            'petitioner': case.petitioner,
        }
        for case in cases
    ]
    return JsonResponse(data, safe=False)

@login_required
def missing_ajax_search_view(request):
    query = request.GET.get('q', '').strip()
    cases = BNSSMissingCase.objects.filter(case_category='Missing', user=request.user)

    if query:
        cases = cases.filter(
            Q(crime_number__icontains=query) |
            Q(petitioner__icontains=query) |
            Q(police_station__icontains=query) |
            Q(date_of_occurrence__icontains=query) |
            Q(date_of_receipt__icontains=query)
        )

    data = [
        {
            'id': case.id,
            'crime_number': case.crime_number,
            'date_of_receipt': case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs'),
            'date_of_occurrence': case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs'),
            'police_station': case.police_station,
            'mps_limit': case.mps_limit,
            'petitioner': case.petitioner,
        }
        for case in cases
    ]
    return JsonResponse(data, safe=False)

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
            ("Police Station", bnss.police_station),  # Directly use it as string
            ("MPS Limit", bnss.mps_limit),
            ("Date of Occurrence", bnss.date_of_occurrence.strftime('%Y-%m-%d %H:%M') if bnss.date_of_occurrence else ''),
            ("Date of Receipt", bnss.date_of_receipt.strftime('%Y-%m-%d') if bnss.date_of_receipt else ''),
            ("Place of Occurrence", bnss.place_of_occurrence),
            ("Petitioner", bnss.petitioner),
            ("Diseased", bnss.diseased if bnss.case_category == '194 BNSS' else ''),
            ("Missing Person", bnss.missing_person if bnss.case_category == 'Missing' else ''),
            ("IO", bnss.io),
            ("Gist of Case", bnss.gist_of_case),
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
            ("Police Station", missing.police_station),  # Directly use it as string
            ("MPS Limit", missing.mps_limit),
            ("Date of Occurrence", missing.date_of_occurrence.strftime('%Y-%m-%d %H:%M') if missing.date_of_occurrence else ''),
            ("Date of Receipt", missing.date_of_receipt.strftime('%Y-%m-%d') if missing.date_of_receipt else ''),
            ("Place of Occurrence", missing.place_of_occurrence),
            ("Petitioner", missing.petitioner),
            ("Diseased", missing.diseased if missing.case_category == '194 BNSS' else ''),
            ("Missing Person", missing.missing_person if missing.case_category == 'Missing' else ''),
            ("IO", missing.io),
            ("Gist of Case", missing.gist_of_case),
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
    add_row('Police Station', case.police_station)
    add_row('MPS Limit', case.mps_limit)
    add_row('Date of Occurrence', case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_occurrence else '')
    add_row('Date of Receipt', case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_receipt else '')
    add_row('Place of Occurrence', case.place_of_occurrence)
    if case.case_category == '194 BNSS':
        add_row('Diseased', case.diseased)
    elif case.case_category == 'Missing':
        add_row('Missing Person', case.missing_person)

    add_row('Petitioner', case.petitioner)
    add_row('IO', case.io)
    add_row('Gist of Case', case.gist_of_case)

    # Prepare response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    filename = f"{case.case_category.replace(' ', '_')}_{case.crime_number}.docx"
    response['Content-Disposition'] = f'attachment; filename={filename}'
    doc.save(response)
    return response

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

@login_required
def bnss_missing_delete_view(request, pk):
    case = get_object_or_404(BNSSMissingCase, pk=pk, user=request.user)
    case.delete()
    return redirect('cases_summary')

@login_required
def othercases_ajax_search_view(request):
    query = request.GET.get('q', '').strip()
    cases = othercases.objects.filter(user=request.user)

    if query:
        cases = cases.filter(
            Q(crime_number__icontains=query) |
            Q(petitioner__icontains=query) |
            Q(police_station__icontains=query) |
            Q(date_of_occurrence__icontains=query) |
            Q(date_of_receipt__icontains=query)
        )

    data = [
        {
            'id': case.id,
            'crime_number': case.crime_number,
            'date_of_receipt': case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs'),
            'date_of_occurrence': case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs'),
            'police_station': case.police_station,
            'mps_limit': case.mps_limit,
            'petitioner': case.petitioner,
        }
        for case in cases
    ]
    return JsonResponse(data, safe=False)

@login_required
def othercases_export_word_view(request):
    other_cases = othercases.objects.filter(user=request.user).order_by('date_of_receipt')
    doc = Document()

    for case in other_cases:
        table = doc.add_table(rows=0, cols=2)
        table.style = 'Table Grid'

        # Fields to include in the Word document
        fields = [
            ("Crime No.", case.crime_number),
            ("Police Station", case.police_station),  # Directly use it as string
            ("MPS Limit", case.mps_limit),
            ("Date of Occurrence", case.date_of_occurrence.strftime('%Y-%m-%d %H:%M') if case.date_of_occurrence else ''),
            ("Date of Receipt", case.date_of_receipt.strftime('%Y-%m-%d') if case.date_of_receipt else ''),
            ("Place of Occurrence", case.place_of_occurrence),
            ("Petitioner", case.petitioner),
            ("Diseased", case.diseased if case.diseased else ''),
            ("Injured", case.injured if case.injured else ''),
            ("Accused", case.accused if case.accused else ''),
            ("IO", case.io),
            ("Gist of Case", case.gist_of_case),
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

@login_required
def othercases_download_view(request, pk):
    case = get_object_or_404(othercases, pk=pk, user=request.user)

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
    add_row('Police Station', case.police_station)
    add_row('MPS Limit', case.mps_limit)
    add_row('Date of Occurrence', case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_occurrence else '')
    add_row('Date of Receipt', case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_receipt else '')
    add_row('Place of Occurrence', case.place_of_occurrence)
    add_row('Petitioner', case.petitioner)
    add_row('Diseased', case.diseased if case.diseased else '')
    add_row('Injured', case.injured if case.injured else '')
    add_row('Accused', case.accused if case.accused else '')
    add_row('IO', case.io)
    add_row('Gist of Case', case.gist_of_case)

    # Prepare response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    filename = f"Other_Case_{case.crime_number}.docx"
    response['Content-Disposition'] = f'attachment; filename={filename}'
    doc.save(response)
    return response

@login_required
def othercases_edit_view(request, pk):
    case = get_object_or_404(othercases, pk=pk, user=request.user)
    if request.method == 'POST':
        form = othercasesForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            messages.success(request, 'Other case updated successfully!')
            return redirect('cases_summary')
    else:
        form = othercasesForm(instance=case)

    return render(request, 'dsr/user/forms/othercases_form.html', {'form': form, 'edit_mode': True})

@login_required
def othercases_delete_view(request, pk):
    case = get_object_or_404(othercases, pk=pk, user=request.user)
    case.delete()
    messages.success(request, 'Other case entry deleted successfully!')
    return redirect('cases_summary')

@login_required
def maritimeact_ajax_search_view(request):
    query = request.GET.get('q', '').strip()
    cases = maritimeact.objects.filter(user=request.user)

    if query:
        cases = cases.filter(
            Q(crime_number__icontains=query) |
            Q(petitioner__icontains=query) |
            Q(police_station__icontains=query) |
            Q(date_of_occurrence__icontains=query) |
            Q(date_of_receipt__icontains=query)
        )

    data = [
        {
            'id': case.id,
            'crime_number': case.crime_number,
            'date_of_receipt': case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs'),
            'date_of_occurrence': case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs'),
            'police_station': case.police_station,
            'mps_limit': case.mps_limit,
            'petitioner': case.petitioner,
        }
        for case in cases
    ]
    return JsonResponse(data, safe=False)

@login_required
def maritimeact_export_word_view(request):
    maritime_cases = maritimeact.objects.filter(user=request.user).order_by('date_of_receipt')
    doc = Document()

    for case in maritime_cases:
        table = doc.add_table(rows=0, cols=2)
        table.style = 'Table Grid'

        # Fields to include in the Word document
        fields = [
            ("Crime No.", case.crime_number),
            ("Police Station", case.police_station),  # Directly use it as string
            ("MPS Limit", case.mps_limit),
            ("Date of Occurrence", case.date_of_occurrence.strftime('%Y-%m-%d %H:%M') if case.date_of_occurrence else ''),
            ("Date of Receipt", case.date_of_receipt.strftime('%Y-%m-%d') if case.date_of_receipt else ''),
            ("Place of Occurrence", case.place_of_occurrence),
            ("Petitioner", case.petitioner),
            ("Accused", case.accused if case.accused else ''),
            ("IO", case.io),
            ("Gist of Case", case.gist_of_case),
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

@login_required
def maritimeact_download_view(request, pk):
    case = get_object_or_404(maritimeact, pk=pk, user=request.user)

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
    add_row('Police Station', case.police_station)
    add_row('MPS Limit', case.mps_limit)
    add_row('Date of Occurrence', case.date_of_occurrence.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_occurrence else '')
    add_row('Date of Receipt', case.date_of_receipt.strftime('%d-%m-%Y %H%Mhrs') if case.date_of_receipt else '')
    add_row('Place of Occurrence', case.place_of_occurrence)
    add_row('Petitioner', case.petitioner)
    add_row('Accused', case.accused if case.accused else '')
    add_row('IO', case.io)
    add_row('Gist of Case', case.gist_of_case)

    # Prepare response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    filename = f"Maritime_Case_{case.crime_number}.docx"
    response['Content-Disposition'] = f'attachment; filename={filename}'
    doc.save(response)
    return response

@login_required
def maritimeact_edit_view(request, pk):
    case = get_object_or_404(maritimeact, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MaritimeActForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            messages.success(request, 'Maritime Act case updated successfully!')
            return redirect('cases_summary')
    else:
        form = MaritimeActForm(instance=case)

    return render(request, 'dsr/user/forms/maritimeact_form.html', {'form': form, 'edit_mode': True})

@login_required
def maritimeact_delete_view(request, pk):
    case = get_object_or_404(maritimeact, pk=pk, user=request.user)
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

