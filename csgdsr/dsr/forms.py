from django import forms

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import CASE_CATEGORIES, MPS_CHOICES, AttackOnTNFishermen_Choices,ArrestOfTNFishermen_Choices,ArrestOfSLFishermen_Choices, CSR,BNSSMissingCase, MaritimeAct, OtherCases, RescueAtBeach, RescueAtSea, Seizure, Officer,SeizedItemCategory,Forecast,AttackOnTNFishermen, ArrestOfTNFishermen, ArrestOfSLFishermen, OnRoadVehicleStatus, OnWaterVehicleStatus,VVCmeeting, BeatDetails, BoatPatrol,Atvpatrol, Proforma,VehicleCheckPost,VehicleCheckothers,CheckPost,Other_Agencies,MPS, CustomUser, PS
from django.core.exceptions import ValidationError
User = get_user_model()
USER_CHOICES = [
    ('ADGP', 'ADGP'),('DIG', 'DIG'),
    ('SP_Nagapattinam', 'SP_Nagapattinam'),('SP_Ramnad', 'SP_Ramnad'),
    ('ADSP_Nagapattinam', 'ADSP_Nagapattinam'),('ADSP_Ramnad', 'ADSP_Ramnad'),
    ('DSP_Chennai', 'DSP_Chennai'),('DSP_Vedaranyam', 'DSP_Vedaranyam'),('DSP_Pattukottai', 'DSP_Pattukottai'),('DSP_Thoothukudi', 'DSP_Thoothukudi'),
    ('INS_Chennai', 'INSChennai'),('INS_Mahaballipuram', 'INS_Mahaballipuram'),('INS_Cuddalore', 'INS_Cuddalore'),('INS_Nagapattinam', 'INS_Nagapattinam'),('INS_Vedaranyam', 'INS_Vedaranyam'),('INS_Pattukottai', 'INS_Pattukottai'),('INS_Manamelkudi', 'INS_Manamelkudi'),('INS_Ramnad', 'INS_Ramnad'),('INS_Thoothukudi', 'INS_Thoothukudi'),('INS_Kanyakumari', 'INS_Kanyakumari'),

    ('Marina_MPS', 'Marina_MPS'),('Ernavur_MPS', 'Ernavur_MPS'),('Pazhaverkadu_MPS', 'Pazhaverkadu_MPS'),
    ('Arambakkam_MPS', 'Arambakkam_MPS'),
    ('Kovalam_MPS', 'Kovalam_MPS'),
    ('Kalpakkam_MPS', 'Kalpakkam_MPS'),
    ('Muthaliyarkuppam_MPS', 'Muthaliyarkuppam_MPS'),
    ('Marakkanam_MPS','Marakkanam_MPS'),
    ('Pudukuppam_MPS','Pudukuppam_MPS'),
    ('Devanampattinam _MPS','Devanampattinam_MPS'), 
    ('Parangipettai_MPS','Parangipettai_MPS'),
    ('Pudupattinam_MPS','Pudupattinam_MPS'),
    ('Thirumullaivasal_MPS','Thirumullaivasal_MPS'), 
    ('Poombuhar_MPS','Poombuhar_MPS'), 
    ('Tharangambadi_MPS','Tharangambadi_MPS'), 
    ('Nagapattinam_MPS','Nagapattinam_MPS'), 
    ('Velankanni_MPS','Velankanni_MPS'), 
    ('Keelaiyur_MPS','Keelaiyur_MPS'), 
    ('Vedaranyam_MPS','Vedaranyam_MPS'), 
    ('Therkukadu_MPS','Therkukadu_MPS'), 
    ('Adhiramapattinam_MPS','Adhiramapattinam_MPS'), 
    ('Sethubavachatiram_MPS','Sethubavachatiram_MPS'), 
    ('Manamelkudi_MPS','Manamelkudi_MPS'), 
    ('Mimisal_MPS','Mimisal_MPS'), 
    ('Thirupunavasal_MPS','Thirupunavasal_MPS'), 
    ('Thondi_MPS','Thondi_MPS'), 
    ('Devipattinam_MPS','Devipattinam_MPS'), 
    ('Attrankarai_MPS','Attrankarai_MPS'), 
    ('Mandapam_MPS','Mandapam_MPS'), 
    ('Rameswaram_MPS','Rameswaram_MPS'), 
    ('Pudumadam_MPS','Pudumadam_MPS'), 
    ('Keelakarai_MPS','Keelakarai_MPS'), 
    ('Valinokkam_MPS','Valinokkam_MPS'),
    ('Vembar_MPS','Vembar_MPS'),
    ('Tharuvaikulam_MPS','Tharuvaikulam_MPS'),
    ('Meenavar_Colony_MPS','Meenavar_Colony_MPS'),
    ('Thiruchendur_MPS','Thiruchendur_MPS'),
    ('Kulasekarapattinam_MPS','Kulasekarapattinam_MPS'),
    ('Uvari_MPS','Uvari_MPS'),
    ('Koodankulam_MPS','Koodankulam_MPS'),
    ('Kanniyakumari_MPS','Kanniyakumari_MPS'),
    ('Colachel_MPS','Colachel_MPS'),('Control_Room', 'Control_Room'),('TBS_SI', 'TBS_SI'),('SI_Tech', 'SI_Tech'),


]



# admin interface forms 

class CustomSignupForm(forms.ModelForm):
    username = forms.ChoiceField(choices=USER_CHOICES, widget=forms.Select(attrs={"class": "form-select"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    role = forms.ChoiceField(
        choices=[('', 'Select Role')] + CustomUser.ROLE_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"})
    )
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Passwords do not match.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Set password
        user.set_password(self.cleaned_data["password1"])
        
        # Assign superuser/staff based on role
        if self.cleaned_data["role"] == "Admin":
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False

        if commit:
            user.save()
        return user
        
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class OfficerForm(forms.ModelForm):
    rank = forms.ChoiceField(
        choices=[('', 'Select Rank')] + Officer.RANK_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Officer
        fields = ['name', 'rank']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Officer Name'}),
        }

class MPSForm(forms.ModelForm):
    class Meta:
        model = MPS
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter MPS Name'}),
        }

class PSForm(forms.ModelForm):
    class Meta:
        model = PS
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PS Name'}),
        }

class CheckPostForm(forms.ModelForm):
    class Meta:
        model = CheckPost
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Checkpost Name'}),
        }

class Other_AgenciesForm(forms.ModelForm):
    class Meta:
        model = Other_Agencies
        fields = ['agency_name']
        widgets = {
            'agency_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Other Agency Name'}),
        }

class AttackOnTNFishermen_ChoicesForm(forms.ModelForm):
    class Meta:
        model = AttackOnTNFishermen_Choices
        fields = ['attacker_name']
        widgets = {
            'attacker_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Attacker Name'}),
        }

class ArrestOfTNFishermen_ChoicesForm(forms.ModelForm):
    class Meta:
        model = ArrestOfTNFishermen_Choices
        fields = ['arrested_by']
        widgets = {
            'arrested_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Arresting Authority Name'}),
        }

class ArrestOfSLFishermen_ChoicesForm(forms.ModelForm):
    class Meta:
        model = ArrestOfSLFishermen_Choices
        fields = ['arrested_by']
        widgets = {
            'arrested_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Arresting Authority Name'}),
        }

class SeizedItemCategoryForm(forms.ModelForm):
    class Meta:
        model = SeizedItemCategory
        fields = ['item_name', 'quantity_type']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Item Name'}),
            'quantity_type': forms.Select(attrs={'class': 'form-control'}),
        }
        
# user interface forms 
class CSRForm(forms.ModelForm):
    class Meta:
        model = CSR
        fields = '__all__'
        labels = {
            'csr_number': 'CSR Number',
            'mps_limit': 'Police Station',
            'date_of_receipt': 'Date of Receipt',
            'place_of_occurrence': 'Place of Occurrence',
            'petitioner': 'Petitioner',
            'counter_petitioner': 'Counter Petitioner',
            'nature_of_petition': 'Nature of Petition',
            'gist_of_petition': 'Gist of Petition',
            'io': 'Investigation Officer',
        }
        widgets = {
            'csr_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter CSR Number'}),
            'mps_limit': forms.Select(attrs={'class': 'form-control',}),
            'date_of_receipt': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'),
            'place_of_occurrence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Occurrence'}),
            'petitioner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Petitioner details'}),
            'counter_petitioner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Counter Petitioner details (if any)'}),
            'nature_of_petition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Nature of Petition'}),
            'io': forms.Select(attrs={'class': 'form-control'}),
            'gist_of_petition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Gist of Petition'}),
        }


class BNSSMissingCaseForm(forms.ModelForm):
    case_category = forms.ChoiceField(
        choices=[('', 'Select Category')] + CASE_CATEGORIES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    ps_limit = forms.ModelChoiceField(
        queryset=PS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Local PS Limit"
    )
    io = forms.ModelChoiceField(
        queryset=Officer.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Investigation Officer"
    )
    transfered_to = forms.ModelChoiceField(
        queryset=Other_Agencies.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Transfered to Agency",
        required=False
    )

    class Meta:
        model = BNSSMissingCase
        exclude = ['submitted_at', 'user']
        widgets = {
            'crime_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Crime Number'}),
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
        }

class othercasesForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    ps_limit = forms.ModelChoiceField(
        queryset=PS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Local PS Limit"
    )
    transfered_to = forms.ModelChoiceField(
        queryset=Other_Agencies.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Transfered to Agency",required=False
    )
    io = forms.ModelChoiceField(
        queryset=Officer.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Investigation Officer"
    )
    class Meta:
        model = OtherCases
        exclude = ['submitted_at', 'user']
        widgets = {
            'crime_number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Crime Number'}),
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
        }

class MaritimeActForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    ps_limit = forms.ModelChoiceField(
        queryset=PS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Local Police Station"
    )
    transfered_to = forms.ModelChoiceField(
        queryset=Other_Agencies.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Transfered to Agency",
        required=False
    )
    io = forms.ModelChoiceField(
        queryset=Officer.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Investigation Officer",
        
    )

    class Meta:
        model = MaritimeAct
        exclude = ['submitted_at', 'user']
        widgets = {
            'crime_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Crime Number'}),
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
        }

class RescueAtBeachForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    ps_limit = forms.ModelChoiceField(
        queryset=PS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Local Police Station"
    )
    class Meta:
        model = RescueAtBeach
        exclude = ['submitted_at', 'user']
        widgets = {
            'date_of_rescue': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'place_of_rescue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Rescue'}),
            'number_of_victims': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Victims Rescued'}),
            'victim_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Victim Names'}),
            'rescuer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Rescuer Names'}),
            'rescue_beach_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'gist_of_rescue': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Rescue details'}),
        }

class RescueAtSeaForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    
    class Meta:
        model = RescueAtSea
        exclude = ['submitted_at', 'user']
        widgets = {
            'date_of_rescue': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'place_of_rescue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Rescue'}),
            'number_of_victims': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Victims Rescued'}),
            'number_of_boats_rescued': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Boats Rescued'}),
            'victim_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Victim Names'}),
            'rescuer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Rescuer Names'}),
            'rescue_sea_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'gist_of_rescue': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Rescue Summary'}),
        }

class SeizureForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    ps_limit = forms.ModelChoiceField(
        queryset=PS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select PS Limit"
    )
    transfered_to = forms.ModelChoiceField(
        queryset=Other_Agencies.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Transfered to Agency"
    )
    

    class Meta:
        model = Seizure
        exclude = ['submitted_at', 'user']
        widgets = {
            'seized_item': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quantity'}),
            'date_of_seizure': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'place_of_seizure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Seizure'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Longitude'}),
            'accused': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Accused Name details & Vehicle No (if any)'}),
            'seized_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Seized By Name'}),
            'seizure_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'gist_of_seizure': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Gist of Seizure'})
        }
   
class ForecastForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    class Meta:
        model = Forecast
        exclude = ['submitted_at', 'user']
        widgets = {
            'date_of_forecast': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'place_of_forecast': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Forecast'}),
            'forecast_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Forecast Details'}),
        }
    
class AttackOnTNFishermenForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    attacked_by = forms.ModelChoiceField(
        queryset=Other_Agencies.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Attacker"
    )
    transfered_to = forms.ModelChoiceField(
        queryset=Other_Agencies.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Transfered to Agency"
    )
    
    class Meta:
        model = AttackOnTNFishermen
        exclude = ['submitted_at', 'user']
        widgets = {
            'date_of_attack': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'place_of_attack': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Attack'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Longitude'}),
            'number_of_TNFishermen_injured': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of TN Fishermen Injured'}),
            'number_of_TNFishermen_died': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of TN Fishermen died'}),
            'number_of_TNFishermen_missing': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of TN Fishermen Missing'}),
            'victim_names': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Victim Names'}),
            'attacker_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Attacker Details'}),
            'items_looted': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Items Looted (if any)'}),
            'gist_of_attack': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Gist of Attack'}),
        }

class ArrestOfTNFishermenForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    arrested_by = forms.ModelChoiceField(
        queryset=Other_Agencies.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Arrested by Agency"
    )
    

    class Meta:
        model = ArrestOfTNFishermen
        exclude = ['submitted_at', 'user']
        widgets = {
            'date_of_arrest': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'place_of_arrest': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Arrest'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Longitude'}),
            'number_of_TNFishermen_arrested': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of TN Fishermen Arrested'}),
            'arrested_Fishermen_names': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Arrested Fishermen Names'}),
            'no_of_boats_seized': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Boats Seized'}),
            'boat_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Boat Details'}),
            'gist_of_arrest': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Gist of Arrest'}),
            'number_of_TNFishermen_released': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of TN Fishermen Released'}),
            'no_of_boats_released': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Boats Released'}),
        }

class ArrestOfSLFishermenForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    arrested_by = forms.ModelChoiceField(
        queryset=Other_Agencies.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Attacker"
    )
    ps_limit = forms.ModelChoiceField(
        queryset=PS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select PS Limit"
    )
    

    class Meta:
        model = ArrestOfSLFishermen
        exclude = ['submitted_at', 'user']
        widgets = {
            'date_of_arrest': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'place_of_arrest': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Arrest'}),
            'number_of_SLFishermen_arrested': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of SL Fishermen Arrested'}),
            'arrested_Fishermen_names': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Arrested Fishermen Names'}),
            'no_of_boats_seized': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Boats Seized'}),
            'boat_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Boat Details'}),
            'gist_of_arrest': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Gist of Arrest'}),
            'number_of_SLFishermen_released': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of SL Fishermen Released'}),
            'no_of_boats_released': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Boats Released'}),
        }

class OnRoadVehicleStatusForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    

    class Meta:
        model = OnRoadVehicleStatus
        exclude = ['submitted_at']
        widgets = {
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'vehicle_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Vehicle Number of vehicle checked'}),
            'working_status': forms.Select(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Remarks'}),
        }

class OnWaterVehicleStatusForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )

    class Meta:
        model = OnWaterVehicleStatus
        exclude = ['submitted_at']
        widgets = {
            'boat_type': forms.Select(attrs={'class': 'form-control'}),
            'boat_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Boat Number of boat checked'}),
            'working_status': forms.Select(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Remarks'}),
        }

class VVCmeetingForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    class Meta:
        model = VVCmeeting
        exclude = ['submitted_at', 'user']
        widgets = { 
            'date_of_vvc': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'village_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Village Name'}),
            'number_of_villagers': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter no. of Villagers attended meeting'}),
            'conducted_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Officer Conducted VVC'}),
            'vvc_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'vvc_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Remarks (if any)'}),
        }

class BeatDetailsForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    day_beat_count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Day Beat Count'}),
        initial=0
    )
    
    night_beat_count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Night Beat Count'}),
        initial=0
    )
    
    class Meta:
        model = BeatDetails
        exclude = ['submitted_at', 'user']
        widgets = {
            'date_of_beat': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }

class ProformaForm(forms.ModelForm):
    mps_visited = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter MPS Visited Count'}),
        initial=0
    )
    check_post_checked = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter no. of Check Post Checked'}),
        initial=0
    )
    boat_guard_checked = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter no. of Boat Guard Checked'}),
        initial=0
    )
    vvc_meeting_conducted = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter no. of VVC Meeting Conducted'}),
        initial=0
    )
    villages_visited = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter no. of Villages Visited'}),
        initial=0
    )
    meetings_attended = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter no. of Meetings Attended'}),
        initial=0
    )
    awareness_programs_conducted = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter no. of Awareness Programs Conducted'}),
        initial=0
    )
    coastal_security_exercises_conducted = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter no. of Coastal Security Exercises Conducted'}),
        initial=0
    )
    class Meta:
        model = Proforma
        exclude = ['submitted_at', 'user']
        widgets = {
            'date_of_proforma': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),        
        }


class BoatPatrolForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    patrol_officer = forms.ModelChoiceField(
        queryset=Officer.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Patrol Officer"
    )
    
    class Meta:
        model = BoatPatrol
        exclude = ['submitted_at', 'user']
        widgets = {
            'boat_type': forms.Select(attrs={'class': 'form-control'}),
            'boat_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Boat Number'}),
            'date_of_patrol': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}),
            'patrol_start_time': forms.TimeInput(
            attrs={'type': 'time', 'class': 'form-control'},
                format='%H:%M'
            ),
            'patrol_end_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'},
                format='%H:%M'
            ),
            'number_of_boats_checked': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Boats Checked'}),
            'registration_numberofboats_checked': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Registration Number of Boats Checked'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Remarks'}),
        }

class AtvpatrolForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    patrol_officer = forms.ModelChoiceField(
        queryset=Officer.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Patrol Officer"
    )
    
    class Meta:
        model = Atvpatrol
        exclude = ['submitted_at', 'user']
        widgets = {
            'atv_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ATV Number'}),
            'date_of_patrol': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'patrol_start_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'},
                format='%H:%M'
            ),
            'patrol_end_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'},
                format='%H:%M'
            ),
            'patrol_place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Patrol Place'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Remarks'}),
        }

class VehicleCheckPostForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    check_post = forms.ModelChoiceField(
    queryset=CheckPost.objects.all(),
    widget=forms.Select(attrs={'class': 'form-control'}),
    empty_label="Select Checkpost"
    )
    officer = forms.ModelChoiceField(
        queryset=Officer.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Officer"
    )
    
    class Meta:
        model = VehicleCheckPost
        exclude = ['submitted_at', 'user']
        widgets = {
            'date_of_check': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'vehicle_check_start_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'},
                format='%H:%M'
            ),
            'vehicle_check_end_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'},
                format='%H:%M'
            ),
            'number_of_vehicles_checked': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Vehicles Checked'}),
            'registration_numbers': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Registration Number of Vehicles Checked'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Remarks'}),
        }

class VehicleCheckothersForm(forms.ModelForm):
    mps_limit = forms.ModelChoiceField(
        queryset=MPS.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select MPS Limit"
    )
    officer = forms.ModelChoiceField(
        queryset=Officer.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Officer"
    )
    
    class Meta:
        model = VehicleCheckothers
        exclude = ['submitted_at', 'user']
        widgets = {
            'date_of_check': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'vehicle_check_start_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'},
                format='%H:%M'
            ),
            'vehicle_check_end_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'},
                format='%H:%M'
            ),
            'place_of_check': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place of Check'}),
            'number_of_vehicles_checked': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Vehicles Checked'}),
            'registration_numbers': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Registration Number of Vehicles Checked'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Remarks'}),
        }