from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import CASE_CATEGORIES, MPS_CHOICES, CSR,BNSSMissingCase, othercases, maritimeact

USER_CHOICES = [
    ('ADGP', 'ADGP'),('DIG', 'DIG'),
    ('SP_Nagapattinam', 'SP_Nagapattinam'),('SP_Ramnad', 'SP_Ramnad'),
    ('ADSP_Nagapattinam', 'ADSP_Nagapattinam'),('ADSP_Ramnad', 'ADSP_Ramnad'),
    ('DSP_Chennai', 'DSP_Chennai'),('DSP_Vedaranyam', 'DSP_Vedaranyam'),('DSP_Pattukottai', 'DSP_Pattukottai'),('DSP_Thoothukudi', 'DSP_Thoothukudi'),
    ('INS_Chennai', 'INSChennai'),('INS_Mahaballipuram', 'INS_Mahaballipuram'),('INS_Cuddalore', 'INS_Cuddalore'),('INS_Nagapattinam', 'INS_Nagapattinam'),('INS_Vedaranyam', 'INS_Vedaranyam'),('INS_Pattukottai', 'INS_Pattukottai'),('INS_Manamelkudi', 'INS_Manamelkudi'),('INS_Ramnad', 'INS_Ramnad'),('INS_Thoothukudi', 'INS_Thoothukudi'),('INS_Kanyakumari', 'INS_Kanyakumari'),
    ('MARINA_MPS', 'MARINA_MPS'),('ERNAVUR_MPS', 'ERNAVUR_MPS'),('PAZHAVERKADU_MPS', 'PAZHAVERKADU_MPS'),
    ('ARAMBAKKAM_MPS', 'ARAMBAKKAM_MPS'),
    ('KOVALAM_MPS', 'KOVALAM_MPS'),
    ('KALPAKKAM_MPS', 'KALPAKKAM_MPS'),
    ('MUTHALIYARKUPPAM_MPS', 'MUTHALIYARKUPPAM_MPS'),
    ('MARAKKANAM_MPS','MARAKKANAM_MPS'),
    ('PUDUKUPPAM_MPS','PUDUKUPPAM_MPS'),
    ('DEVANAMPATTINAM _MPS','DEVANAMPATTINAM_MPS'), 
    ('PARANGIPETTAI_MPS','PARANGIPETTAI_MPS'),
    ('PUDUPATTINAM_MPS','PUDUPATTINAM_MPS'),
    ('THIRUMULLAIVASAL_MPS','THIRUMULLAIVASAL_MPS'), 
    ('POOMBUHAR_MPS','POOMBUHAR_MPS'), 
    ('THARANGAMBADI_MPS','THARANGAMBADI_MPS'), 
    ('NAGAPATTINAM_MPS','NAGAPATTINAM_MPS'), 
    ('VELANKANNI_MPS','VELANKANNI_MPS'), 
    ('KEELAIYUR_MPS','KEELAIYUR_MPS'), 
    ('VEDARANYAM_MPS','VEDARANYAM_MPS'), 
    ('THERKUKADU_MPS','THERKUKADU_MPS'), 
    ('ADHIRAMAPATTINAM_MPS','ADHIRAMAPATTINAM_MPS'), 
    ('SETHUBAVACHATIRAM_MPS','SETHUBAVACHATIRAM_MPS'), 
    ('MANAMELKUDI_MPS','MANAMELKUDI_MPS'), 
    ('MIMISAL_MPS','MIMISAL_MPS'), 
    ('THIRUPUNAVASAL_MPS','THIRUPUNAVASAL_MPS'), 
    ('THONDI_MPS','THONDI_MPS'), 
    ('DEVIPATTINAM_MPS','DEVIPATTINAM_MPS'), 
    ('ATTRANKARAI_MPS','ATTRANKARAI_MPS'), 
    ('MANDAPAM_MPS','MANDAPAM_MPS'), 
    ('RAMESWARAM_MPS','RAMESWARAM_MPS'), 
    ('PUDUMADAM_MPS','PUDUMADAM_MPS'), 
    ('KEELAKARAI_MPS','KEELAKARAI_MPS'), 
    ('VALINOKKAM_MPS','VALINOKKAM_MPS'),
    ('VEMBAR_MPS','VEMBAR_MPS'),
    ('THARUVAIKULAM_MPS','THARUVAIKULAM_MPS'),
    ('MEENAVAR_COLONY_MPS','MEENAVAR_COLONY_MPS'),
    ('THIRUCHENDUR_MPS','THIRUCHENDUR_MPS'),
    ('KULASEKARAPATTINAM_MPS','KULASEKARAPATTINAM_MPS'),
    ('UVARI_MPS','UVARI_MPS'),
    ('KOODANKULAM_MPS','KOODANKULAM_MPS'),
    ('KANNIYAKUMARI_MPS','KANNIYAKUMARI_MPS'),
    ('COLACHEL_MPS','COLACHEL_MPS') 
]


class CustomSignupForm(forms.ModelForm):
    username = forms.ChoiceField(choices=USER_CHOICES, widget=forms.Select(attrs={"class": "form-select"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class CSRForm(forms.ModelForm):
    class Meta:
        model = CSR
        fields = '__all__'
        labels = {
            'csr_number': 'CSR Number',
            'police_station': 'Police Station',
            'date_of_receipt': 'Date of Receipt',
            'place_of_occurrence': 'Place of Occurrence',
            'petitioner': 'Petitioner',
            'counter_petitioner': 'Counter Petitioner',
            'nature_of_petition': 'Nature of Petition',
            'gist_of_petition': 'Gist of Petition',
        }
        widgets = {
            'csr_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 202/2025'}),
            'police_station': forms.Select(attrs={'class': 'form-control',}),
            'date_of_receipt': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'),
            'place_of_occurrence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Occurrence'}),
            'petitioner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Petitioner details'}),
            'counter_petitioner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Counter Petitioner details (if any)'}),
            'nature_of_petition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Nature of Petition'}),
            'gist_of_petition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Gist of Petition'}),
        }


class BNSSMissingCaseForm(forms.ModelForm):
    case_category = forms.ChoiceField(
        choices=[('', 'Select Category')] + CASE_CATEGORIES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    mps_limit = forms.ChoiceField(
        choices=[('', 'Select MPS Limit')] + MPS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = BNSSMissingCase
        exclude = ['submitted_at', 'user']
        widgets = {
            'crime_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Crime Number'}),
            'police_station': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Police Station'}),
            'date_of_occurrence': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'date_of_receipt': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'place_of_occurrence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Occurrence'}),
            'diseased': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Deceased Name (if any)'}),
            'missing_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Missing Person Name'}),
            'petitioner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Petitioner Name'}),
            'gist_of_case': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Gist of Case'}),
            'io': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Investigation Officer'}),
        }

class othercasesForm(forms.ModelForm):
    class Meta:
        model = othercases
        exclude = ['submitted_at', 'user']
        widgets = {
            'crime_number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Crime Number'}),
            'police_station': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Police Station'}),
            'mps_limit': forms.Select(attrs={'class': 'form-control'}),
            'date_of_occurrence': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'date_of_receipt': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'place_of_occurrence': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Place of Occurrence'}),
            'petitioner': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Petitioner details'}),
            'diseased': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Diseased detail (if any)'}),
            'injured': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter injured person details (if any)'}),
            'accused': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Accused details (if any)'}),
            'gist_of_case': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Gist of Case'}),
            'io': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Investigation Officer Name and Rank'}),
        }

class MaritimeActForm(forms.ModelForm):
    mps_limit = forms.ChoiceField(
        choices=[('', 'Select MPS Limit')] + MPS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = maritimeact
        exclude = ['submitted_at', 'user']
        widgets = {
            'crime_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Crime Number'}),
            'police_station': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Police Station'}),
            'date_of_occurrence': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'date_of_receipt': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'place_of_occurrence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Occurrence'}),
            'petitioner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Petitioner Name'}),
            'accused': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Accused details (if any)'}),
            'gist_of_case': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Gist of Case'}),
            'io': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Investigation Officer Name and Rank'}),
        }