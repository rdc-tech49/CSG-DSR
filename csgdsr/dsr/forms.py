from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

USER_CHOICES = [
    ('ADGP', 'ADGP'),('DIG', 'DIG'),('SP Nagapattinam', 'SP Nagapattinam'),('SP Ramnad', 'SP Ramnad'),
    ('ADSP Nagapattinam', 'ADSP Nagapattinam'),('ADSP Ramnad', 'ADSP Ramnad'),
    ('DSP Chennai', 'DSP Chennai'),('DSP Vedaranyam', 'DSP Vedaranyam'),('DSP Pattukottai', 'DSP Pattukottai'),('DSP Thoothukudi', 'DSP Thoothukudi'),
    ('INS Chennai', 'INS Chennai'),('INS Mahaballipuram', 'INS Mahaballipuram'),('INS Cuddalore', 'INS Cuddalore'),('INS Nagapattinam', 'INS Nagapattinam'),('INS Vedaranyam', 'INS Vedaranyam'),('INS Pattukottai', 'INS Pattukottai'),('INS Manamelkudi', 'INS Manamelkudi'),('INS Ramnad', 'INS Ramnad'),('INS Thoothukudi', 'INS Thoothukudi'),('INS Kanyakumari', 'INS Kanyakumari'),('SI MARINA', 'SI MARINA'),('SI ERNAVUR', 'SI ERNAVUR'),('SI PAZHAVERKADU', 'SI PAZHAVERKADU'),('SI ARAMBAKKAM', 'SI ARAMBAKKAM'),
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
