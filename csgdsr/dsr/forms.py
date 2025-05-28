from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

USER_CHOICES = [
    ('ADGP', 'ADGP'),('DIG', 'DIG'),
    ('SP Nagapattinam', 'SP Nagapattinam'),('SP Ramnad', 'SP Ramnad'),
    ('ADSP Nagapattinam', 'ADSP Nagapattinam'),('ADSP Ramnad', 'ADSP Ramnad'),
    ('DSP Chennai', 'DSP Chennai'),('DSP Vedaranyam', 'DSP Vedaranyam'),('DSP Pattukottai', 'DSP Pattukottai'),('DSP Thoothukudi', 'DSP Thoothukudi'),
    ('INS Chennai', 'INS Chennai'),('INS Mahaballipuram', 'INS Mahaballipuram'),('INS Cuddalore', 'INS Cuddalore'),('INS Nagapattinam', 'INS Nagapattinam'),('INS Vedaranyam', 'INS Vedaranyam'),('INS Pattukottai', 'INS Pattukottai'),('INS Manamelkudi', 'INS Manamelkudi'),('INS Ramnad', 'INS Ramnad'),('INS Thoothukudi', 'INS Thoothukudi'),('INS Kanyakumari', 'INS Kanyakumari'),
    ('MARINA MPS', 'MARINA MPS'),('ERNAVUR MPS', 'ERNAVUR MPS'),('PAZHAVERKADU MPS', 'PAZHAVERKADU MPS'),
    ('ARAMBAKKAM MPS', 'ARAMBAKKAM'),
    ('KOVALAM MPS', 'KOVALAM'),
    ('KALPAKKAM MPS', 'KALPAKKAM'),
    ('MUTHALIYARKUPPAM MPS', 'MUTHALIYARKUPPAM'),
    ('MARAKKANAM MPS','MARAKKANAM'),
    ('PUDUKUPPAM MPS','PUDUKUPPAM'),
    ('DEVANAMPATTINAM  MPS','DEVANAMPATTINAM MPS'), 
    ('PARANGIPETTAI MPS','PARANGIPETTAI MPS'),
    ('PUDUPATTINAM MPS','PUDUPATTINAM MPS'),
    ('THIRUMULLAIVASAL MPS','THIRUMULLAIVASAL MPS'), 
    ('POOMBUHAR MPS','POOMBUHAR MPS'), 
    ('THARANGAMBADI MPS','THARANGAMBADI MPS'), 
    ('NAGAPATTINAM MPS','NAGAPATTINAM MPS'), 
    ('VELANKANNI MPS','VELANKANNI MPS'), 
    ('KEELAIYUR MPS','KEELAIYUR MPS'), 
    ('VEDARANYAM MPS','VEDARANYAM MPS'), 
    ('THERKUKADU MPS','THERKUKADU MPS'), 
    ('ADHIRAMAPATTINAM MPS','ADHIRAMAPATTINAM MPS'), 
    ('SETHUBAVACHATIRAM MPS','SETHUBAVACHATIRAM MPS'), 
    ('MANAMELKUDI MPS','MANAMELKUDI MPS'), 
    ('MIMISAL MPS','MIMISAL MPS'), 
    ('THIRUPUNAVASAL MPS','THIRUPUNAVASAL MPS'), 
    ('THONDI MPS','THONDI MPS'), 
    ('DEVIPATTINAM MPS','DEVIPATTINAM MPS'), 
    ('ATTRANKARAI MPS','ATTRANKARAI MPS'), 
    ('MANDAPAM MPS','MANDAPAM MPS'), 
    ('RAMESWARAM MPS','RAMESWARAM MPS'), 
    ('PUDUMADAM MPS','PUDUMADAM MPS'), 
    ('KEELAKARAI MPS','KEELAKARAI MPS'), 
    ('VALINOKKAM MPS','VALINOKKAM MPS'),
    ('VEMBAR MPS','VEMBAR MPS'),
    ('THARUVAIKULAM MPS','THARUVAIKULAM MPS'),
    ('MEENAVAR COLONY MPS','MEENAVAR COLONY MPS'),
    ('THIRUCHENDUR MPS','THIRUCHENDUR MPS'),
    ('KULASEKARAPATTINAM MPS','KULASEKARAPATTINAM MPS'),
    ('UVARI MPS','UVARI MPS'),
    ('KOODANKULAM MPS','KOODANKULAM MPS'),
    ('KANNIYAKUMARI MPS','KANNIYAKUMARI MPS'),
    ('COLACHEL MPS','COLACHEL MPS') 
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
