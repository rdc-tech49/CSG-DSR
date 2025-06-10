
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils import timezone
from django.core.validators import FileExtensionValidator

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

class SeizedItemCategory(models.Model):
    item_name = models.CharField(max_length=100, unique=True)
    quantity_type = models.CharField(max_length=50, choices=[('kg', 'Kilograms'), ('liters', 'Liters'), ('nos', 'Numbers')])
    def __str__(self):
        return self.item_name

Other_Agencies = [
    ('Indian Coast Guard', 'Indian Coast Guard'),('Indian Navy', 'Indian Navy'),('Customs Department', 'Customs Department'), ('Fisheries Department', 'Fisheries Department'),('Forest Department', 'Forest Department'),('Civil Supplies CID', 'Civil Supplies CID'),('Revenue Department', 'Revenue Department'),('Local Police Station', 'Local Police Station'),('Marine Enforcement Wing','Marine Enforcement Wing'),('Other', 'Other')]

CASE_CATEGORIES = [
    
    ('194 BNSS', '194 BNSS'),
    ('Missing', 'Missing'),
]

AttackOnTNFishermen_Choices = [('Sri Lankan Navy', 'Sri Lankan Navy'),('Sri Lankan Fishermen', 'Sri Lankan Fishermen'),('Pirates', 'Pirates'),('Other', 'Other')]

ArrestOfTNFishermen_Choices = [('Sri Lankan Navy', 'Sri Lankan Navy'),('other country Navy', 'Other Country Navy')]

ArrestOfSLFishermen_Choices = [('Indian Navy', 'Indian Navy'),('Indian Coast Guard', 'Indian Coast Guard'), ('Coastal Security Group','Coastal Security Group'),('Other', 'Other')]

class CSR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    csr_number = models.CharField(max_length=20)
    police_station = models.CharField(max_length=50, choices=MPS_CHOICES)
    date_of_receipt = models.DateTimeField()
    place_of_occurrence = models.CharField(max_length=255)
    petitioner = models.CharField(max_length=255)
    counter_petitioner = models.CharField(max_length=255, blank=True, null=True)
    nature_of_petition = models.TextField(null=True)
    gist_of_petition = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
      # stores the logged-in user
 
    def __str__(self):
        return f"{self.csr_number} - {self.police_station}"

class BNSSMissingCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    case_category = models.CharField(max_length=20, choices=CASE_CATEGORIES)
    crime_number = models.CharField(max_length=50)
    police_station = models.CharField(max_length=100)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES)
    date_of_occurrence = models.DateTimeField()
    date_of_receipt = models.DateTimeField()
    place_of_occurrence = models.CharField(max_length=200)
    diseased = models.CharField(max_length=200, blank=True, null=True)
    missing_person = models.CharField(max_length=200, blank=True, null=True)
    petitioner = models.CharField(max_length=100)
    gist_of_case = models.TextField()
    io=models.CharField(max_length=100,blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.case_category} - {self.crime_number} - {self.mps_limit}"
    

class othercases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    crime_number = models.CharField(max_length=50)
    police_station = models.CharField(max_length=100)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES)
    date_of_occurrence = models.DateTimeField()
    date_of_receipt = models.DateTimeField()
    place_of_occurrence = models.CharField(max_length=200)
    petitioner = models.CharField(max_length=100)
    diseased = models.CharField(max_length=200, blank=True, null=True)
    injured = models.CharField(max_length=200, blank=True, null=True)
    accused = models.CharField(max_length=200, blank=True, null=True)
    gist_of_case = models.TextField()
    io=models.CharField(max_length=100,blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.crime_number} - {self.mps_limit}"

class maritimeact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    crime_number = models.CharField(max_length=50)
    police_station = models.CharField(max_length=100)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES)
    date_of_occurrence = models.DateTimeField()
    date_of_receipt = models.DateTimeField()
    place_of_occurrence = models.CharField(max_length=200)
    petitioner = models.CharField(max_length=100)
    accused = models.CharField(max_length=200, blank=True, null=True)
    gist_of_case = models.TextField()
    io=models.CharField(max_length=100,blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crime_number} - {self.mps_limit}"

class RescueAtBeach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    rescue_id = models.AutoField(primary_key=True)
    date_of_rescue = models.DateTimeField()
    place_of_rescue = models.CharField(max_length=200)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES)
    number_of_victims = models.PositiveIntegerField()
    victim_name = models.CharField(max_length=200)
    rescuer_name = models.CharField(max_length=200)
    rescue_beach_image = models.ImageField(upload_to='rescue__beach_images/', blank=True, null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic'])])
    gist_of_rescue = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rescue_id} - {self.victim_name} - {self.date_of_rescue}"
    
class RescueAtSea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    rescue_id = models.AutoField(primary_key=True)
    date_of_rescue = models.DateTimeField()
    place_of_rescue = models.CharField(max_length=200)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES)
    number_of_victims = models.PositiveIntegerField()
    number_of_boats_involved = models.PositiveIntegerField()
    victim_name = models.CharField(max_length=200)
    rescuer_name = models.CharField(max_length=200)
    rescue_sea_image = models.ImageField(upload_to='rescue_sea_images/', blank=True, null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic'])])
    gist_of_rescue = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rescue_id} - {self.victim_name} - {self.date_of_rescue}"
    
class Seizure(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    seizure_id = models.AutoField(primary_key=True)
    seized_item = models.ForeignKey(SeizedItemCategory, on_delete=models.CASCADE)
    quantity = models.FloatField(help_text="Enter quantity in selected unit")
    date_of_seizure = models.DateTimeField()
    place_of_seizure = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES)
    accused = models.CharField(max_length=200, blank=True, null=True)
    seized_by = models.CharField(max_length=200)
    handed_over_to = models.CharField(max_length=200, choices=Other_Agencies, blank=True, null=True)
    seizure_image = models.ImageField(upload_to='seizure_images/', blank=True, null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic'])])
    gist_of_seizure = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.seizure_id} - {self.seized_item}"
    
class Forecast(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    forecast_id = models.AutoField(primary_key=True)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES)
    date_of_forecast = models.DateField()
    forecast_details = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.forecast_id} - {self.mps_limit} - {self.date_of_forecast}"

class AttackOnTNFishermen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    attack_id = models.AutoField(primary_key=True)
    attacked_by = models.CharField(max_length=200, choices=AttackOnTNFishermen_Choices)
    date_of_attack = models.DateField()
    place_of_attack = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES)
    number_of_TNFishermen_injured = models.PositiveIntegerField()
    number_of_TNFishermen_missing = models.PositiveIntegerField(blank=True, null=True)
    number_of_TNFishermen_died = models.PositiveIntegerField(blank=True, null=True)
    victim_names = models.CharField(max_length=200)
    attacker_names = models.CharField(max_length=200, blank=True, null=True)
    items_looted= models.CharField(max_length=200, blank=True, null=True)
    gist_of_attack = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.attack_id} - {self.date_of_attack}"

class ArrestOfTNFishermen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    arrest_id = models.AutoField(primary_key=True)
    date_of_arrest = models.DateField()
    place_of_arrest = models.CharField(max_length=200)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES)
    arrested_by = models.CharField(max_length=200, choices=ArrestOfTNFishermen_Choices)
    number_of_TNFishermen_arrested = models.PositiveIntegerField()
    arrested_Fishermen_name = models.CharField(max_length=200)
    no_of_boats_seized = models.PositiveIntegerField(blank=True, null=True)
    boat_details = models.CharField(max_length=200, blank=True, null=True)
    gist_of_arrest = models.TextField()
    number_of_TNFishermen_released = models.PositiveIntegerField(blank=True, null=True)
    no_of_boats_released = models.PositiveIntegerField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.arrest_id} - {self.date_of_arrest}"

class ArrestOfSLFishermen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    arrest_id = models.AutoField(primary_key=True)
    date_of_arrest = models.DateTimeField()
    place_of_arrest = models.CharField(max_length=200)
    mps_limit = models.CharField(max_length=100, choices=MPS_CHOICES)
    arrested_by = models.CharField(max_length=200, choices=ArrestOfSLFishermen_Choices)
    number_of_SLFishermen_arrested = models.PositiveIntegerField()
    arrested_Fishermen_name = models.CharField(max_length=200)
    no_of_boats_seized = models.PositiveIntegerField(blank=True, null=True)
    boat_details = models.CharField(max_length=200, blank=True, null=True)
    gist_of_arrest = models.TextField()
    number_of_SLFishermen_released = models.PositiveIntegerField(blank=True, null=True)
    no_of_boats_released = models.PositiveIntegerField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.arrest_id} - {self.date_of_arrest}"
