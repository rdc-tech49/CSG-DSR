
from django.db import models

MPS_CHOICES = [
    ("MARINA MPS", "MARINA MPS"),("ERNAVUR MPS", "ERNAVUR MPS"),("PAZHAVERKADU MPS", "PAZHAVERKADU MPS"),
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

FIR_CATEGORIES = [
    ("194 BNSS", "194 BNSS"),
    ("Missing", "Missing"),
    ("Maritime Act", "Maritime Act"),
    ("NDPS", "NDPS"),
    ("102 BNSS", "102 BNSS"),
    ("294 BNS", "294 BNS"),
    ("BNS (others)", "BNS (others)"),
]

class CSR(models.Model):
    csr_no = models.CharField(max_length=20)
    case_registered = models.CharField(max_length=50, choices=MPS_CHOICES)
    mps_limit = models.CharField(max_length=50, choices=MPS_CHOICES)
    date_of_occurrence = models.DateField()
    date_of_receipt = models.DateField()
    scene_of_crime = models.TextField()
    petitioner = models.CharField(max_length=255)
    gist_of_case = models.TextField()

class FIR(models.Model):
    category = models.CharField(max_length=50, choices=FIR_CATEGORIES)
    crime_number = models.CharField(max_length=20)
    case_registered = models.CharField(max_length=50, choices=MPS_CHOICES)
    mps_limit = models.CharField(max_length=50, choices=MPS_CHOICES)
    date_of_occurrence = models.DateField()
    date_of_receipt = models.DateField()
    scene_of_crime = models.TextField()
    petitioner = models.CharField(max_length=255)
    accused = models.CharField(max_length=255, blank=True, null=True)
    deceased = models.CharField(max_length=255, blank=True, null=True)
    missing = models.CharField(max_length=255, blank=True, null=True)
    gist_of_case = models.TextField()
    investigation_officer = models.CharField(max_length=255)

