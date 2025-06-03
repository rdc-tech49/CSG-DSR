
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils import timezone


MPS_CHOICES = [
    ("-- Select Police Station --","-- Select Police Station --"),("MARINA MPS", "MARINA MPS"),("ERNAVUR MPS", "ERNAVUR MPS"),("PAZHAVERKADU MPS", "PAZHAVERKADU MPS"),
    ("ARAMBAKKAM MPS", "ARAMBAKKAM MPS"),
    ("KOVALAM MPS", "KOVALAM MPS"),
    ("KALPAKKAM MPS", "KALPAKKAM MPS"),
    ("MUTHALIYARKUPPAM MPS", "MUTHALIYARKUPPAM MPS"),
    ("MARAKKANAM MPS","MARAKKANAM MPS"),
    ("PUDUKUPPAM MPS","PUDUKUPPAM MPS"),
    ("DEVANAMPATTINAM  MPS","DEVANAMPATTINAM MPS"), 
    ("PARANGIPETTAI MPS","PARANGIPETTAI MPS"),
    ("PUDUPATTINAM MPS","PUDUPATTINAM MPS"),
    ("THIRUMULLAIVASAL MPS","THIRUMULLAIVASAL MPS"), 
    ("POOMBUHAR MPS","POOMBUHAR MPS"), 
    ("THARANGAMBADI MPS","THARANGAMBADI MPS"), 
    ("NAGAPATTINAM MPS","NAGAPATTINAM MPS"), 
    ("VELANKANNI MPS","VELANKANNI MPS"), 
    ("KEELAIYUR MPS","KEELAIYUR MPS"), 
    ("VEDARANYAM MPS","VEDARANYAM MPS"), 
    ("THERKUKADU MPS","THERKUKADU MPS"), 
    ("ADHIRAMAPATTINAM MPS","ADHIRAMAPATTINAM MPS"), 
    ("SETHUBAVACHATIRAM MPS","SETHUBAVACHATIRAM MPS"), 
    ("MANAMELKUDI MPS","MANAMELKUDI MPS"), 
    ("MIMISAL MPS","MIMISAL MPS"), 
    ("THIRUPUNAVASAL MPS","THIRUPUNAVASAL MPS"), 
    ("THONDI MPS","THONDI MPS"), 
    ("DEVIPATTINAM MPS","DEVIPATTINAM MPS"), 
    ("ATTRANKARAI MPS","ATTRANKARAI MPS"), 
    ("MANDAPAM MPS","MANDAPAM MPS"), 
    ("RAMESWARAM MPS","RAMESWARAM MPS"), 
    ("PUDUMADAM MPS","PUDUMADAM MPS"), 
    ("KEELAKARAI MPS","KEELAKARAI MPS"), 
    ("VALINOKKAM MPS","VALINOKKAM MPS"),
    ("VEMBAR MPS","VEMBAR MPS"),
    ("THARUVAIKULAM MPS","THARUVAIKULAM MPS"),
    ("MEENAVAR COLONY MPS","MEENAVAR COLONY MPS"),
    ("THIRUCHENDUR MPS","THIRUCHENDUR MPS"),
    ("KULASEKARAPATTINAM MPS","KULASEKARAPATTINAM MPS"),
    ("UVARI MPS","UVARI MPS"),
    ("KOODANKULAM MPS","KOODANKULAM MPS"),
    ("KANNIYAKUMARI MPS","KANNIYAKUMARI MPS"),
    ("COLACHEL MPS","COLACHEL MPS")
]


CASE_CATEGORIES = [
    ('194 BNSS', '194 BNSS'),
    ('Missing', 'Missing'),
]

class CSR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    csr_number = models.CharField(max_length=20)
    police_station = models.CharField(max_length=50, choices=MPS_CHOICES, default="-- Select Police Station --")
    date_of_receipt = models.DateField()
    place_of_occurrence = models.CharField(max_length=255)
    petitioner = models.CharField(max_length=255)
    counter_petitioner = models.CharField(max_length=255, blank=True, null=True)
    nature_of_petition = models.TextField(null=True)
    gist_of_petition = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
      # stores the logged-in user
 
    def __str__(self):
        return self.csr_number

class BNSSMissingCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    case_category = models.CharField(max_length=20, choices=CASE_CATEGORIES)
    crime_number = models.CharField(max_length=50)
    police_station = models.CharField(max_length=100)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES,default="-- Select Police Station --")
    date_of_occurrence = models.DateTimeField(default=timezone.now)
    date_of_receipt = models.DateTimeField(default=timezone.now)
    place_of_occurrence = models.CharField(max_length=200)
    diseased = models.CharField(max_length=200, blank=True, null=True)
    missing_person = models.CharField(max_length=200, blank=True, null=True)
    petitioner = models.CharField(max_length=100)
    gist_of_case = models.TextField()
    io=models.CharField(max_length=100,blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.case_category} - {self.crime_number}"