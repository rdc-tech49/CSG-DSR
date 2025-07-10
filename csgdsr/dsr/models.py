
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
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

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='User')

    def __str__(self):
        return f"{self.username} ({self.role})"
    
class Officer(models.Model):
    RANK_CHOICES = [
        ('ADGP', 'Additional Director General of Police (ADGP)'),('IG', 'Inspector General of Police (IG)'),
        ('DIG', 'Deputy Inspector General (DIG)'),
        ('SP', 'Superintendent of Police (SP)'),('ASP', 'Assistant Superintendent of Police (ASP)'),('AdSP', 'Additional Superintendent of Police (AdSP)'),
        ('DSP', 'Deputy Superintendent of Police (DSP)'),
        ('INS', 'Inspector (INS)'),
        ('SI', 'Sub-Inspector (SI)'),
        ('SSI', 'Senior Sub-Inspector (SSI)'),     
        ('HAV', 'Havildar (HAV)'),
        ('HC', 'Head Constable (HC)'),
        ('GrI', 'Grade I Constable (GrI)'),
        ('PC', 'Police Constable (PC)'),
        ('TBS SI', 'TBS Sub-Inspector (TBS SI)'),
        ('TBS HC', 'TBS Head Constable (TBS HC)'),
    ]

    name = models.CharField(max_length=255)
    rank = models.CharField(max_length=10, choices=RANK_CHOICES)

    def __str__(self):
        return f"{self.rank} - {self.name}"

CASE_CATEGORIES = [
    
    ('194 BNSS', '194 BNSS'),
    ('Missing', 'Missing'),
]

class MPS(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name.replace("_", " ")

class PS(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class CheckPost(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Other_Agencies(models.Model):
    agency_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.agency_name

class AttackOnTNFishermen_Choices(models.Model):
    attacker_name=models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.attacker_name

class ArrestOfTNFishermen_Choices(models.Model):
    arrested_by=models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.arrested_by

class ArrestOfSLFishermen_Choices(models.Model):
    arrested_by=models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.arrested_by

class SeizedItemCategory(models.Model):
    item_name = models.CharField(max_length=100, unique=True)
    quantity_type = models.CharField(max_length=50, choices=[('kg', 'Kilograms'), ('liters', 'Liters'), ('nos', 'Numbers')])
    def __str__(self):
        return f"{self.item_name} - {self.quantity_type}"



class CSR(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    csr_number = models.CharField(max_length=20)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_receipt = models.DateTimeField()
    place_of_occurrence = models.CharField(max_length=255)
    petitioner = models.CharField(max_length=255)
    counter_petitioner = models.CharField(max_length=255, blank=True, null=True)
    nature_of_petition = models.TextField(null=True)
    gist_of_petition = models.TextField()
    io=models.ForeignKey('Officer', on_delete=models.CASCADE,null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
      # stores the logged-in user
 
    def __str__(self):
        return f"{self.csr_number} - {self.police_station}"

class BNSSMissingCase(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    case_category = models.CharField(max_length=20, choices=CASE_CATEGORIES)
    crime_number = models.CharField(max_length=50)
    ps_limit = models.ForeignKey(PS, on_delete=models.SET_NULL, null=True, blank=True)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_occurrence = models.DateTimeField()
    date_of_receipt = models.DateTimeField()
    place_of_occurrence = models.CharField(max_length=200)
    petitioner = models.CharField(max_length=100)
    diseased = models.CharField(max_length=200, blank=True, null=True)
    missing_person = models.CharField(max_length=200, blank=True, null=True)
    gist_of_case = models.TextField()
    io=models.ForeignKey('Officer', on_delete=models.CASCADE,null=True, blank=True)
    transfered_to = models.ForeignKey(Other_Agencies, on_delete=models.SET_NULL, null=True, blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.case_category} - {self.crime_number} - {self.mps_limit}"
    

class OtherCases(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    crime_number = models.CharField(max_length=50)
    ps_limit = models.ForeignKey(PS, on_delete=models.SET_NULL, null=True, blank=True)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_occurrence = models.DateTimeField()
    date_of_receipt = models.DateTimeField()
    place_of_occurrence = models.CharField(max_length=200)
    petitioner = models.CharField(max_length=100)
    diseased = models.CharField(max_length=200, blank=True, null=True)
    injured = models.CharField(max_length=200, blank=True, null=True)
    accused = models.CharField(max_length=200, blank=True, null=True)
    gist_of_case = models.TextField()
    io=models.ForeignKey('Officer', on_delete=models.CASCADE,null=True, blank=True)
    transfered_to = models.ForeignKey(Other_Agencies, on_delete=models.SET_NULL, null=True, blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.crime_number} - {self.mps_limit}"

class MaritimeAct(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    crime_number = models.CharField(max_length=50)
    ps_limit = models.ForeignKey(PS, on_delete=models.SET_NULL, null=True, blank=True)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_occurrence = models.DateTimeField()
    date_of_receipt = models.DateTimeField()
    place_of_occurrence = models.CharField(max_length=200)
    petitioner = models.CharField(max_length=100)
    accused = models.CharField(max_length=200, blank=True, null=True)
    gist_of_case = models.TextField()
    io=models.ForeignKey('Officer', on_delete=models.CASCADE,null=True, blank=True)
    transfered_to = models.ForeignKey(Other_Agencies, on_delete=models.SET_NULL, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crime_number} - {self.mps_limit}"

class RescueAtBeach(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    date_of_rescue = models.DateTimeField()
    place_of_rescue = models.CharField(max_length=200)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    ps_limit = models.ForeignKey(PS, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_victims = models.PositiveIntegerField()
    victim_name = models.CharField(max_length=200)
    rescuer_name = models.CharField(max_length=200)
    rescue_beach_image = models.ImageField(upload_to='rescue__beach_images/', blank=True, null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic'])])
    gist_of_rescue = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_of_rescue} - {self.place_of_rescue} - {self.number_of_victims} Victims"
    
class RescueAtSea(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    date_of_rescue = models.DateTimeField()
    place_of_rescue = models.CharField(max_length=200)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_victims = models.PositiveIntegerField()
    number_of_boats_rescued = models.PositiveIntegerField(null=True, blank=True)
    victim_name = models.CharField(max_length=200)
    rescuer_name = models.CharField(max_length=200)
    rescue_sea_image = models.ImageField(upload_to='rescue_sea_images/', blank=True, null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic'])])
    gist_of_rescue = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_of_rescue} - {self.place_of_rescue} - {self.number_of_victims} Victims - {self.number_of_boats_rescued} Boats Rescued"
    
class Seizure(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    seized_item = models.ForeignKey(SeizedItemCategory, on_delete=models.CASCADE)
    quantity = models.FloatField(help_text="Enter quantity in selected unit")
    date_of_seizure = models.DateTimeField()
    place_of_seizure = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    ps_limit = models.ForeignKey(PS, on_delete=models.SET_NULL, null=True, blank=True)
    accused = models.CharField(max_length=200, blank=True, null=True)
    seized_by = models.CharField(max_length=200)
    handed_over_to = models.ForeignKey(Other_Agencies, on_delete=models.SET_NULL, null=True, blank=True) 
    seizure_image = models.ImageField(upload_to='seizure_images/', blank=True, null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic'])])
    gist_of_seizure = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_of_seizure} - {self.place_of_seizure} - {self.seized_item.item_name if self.seized_item else ''} - {self.quantity} {self.seized_item.quantity_type if self.seized_item else ''}"

    
class Forecast(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_forecast = models.DateField()
    place_of_forecast = models.CharField(max_length=200)
    forecast_details = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_of_forecast} - {self.place_of_forecast} - {self.mps_limit}"

class AttackOnTNFishermen(models.Model):
    DISTRICT_CHOICES = [
        ('Chennai', 'Chennai'),
        ('Chengalpattu', 'Chengalpattu'),
        ('Villupuram', 'Villupuram'),
        ('Rameswaram', 'Rameswaram'),
        ('Cuddalore', 'Cuddalore'),
    ]
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    attacked_by = models.ForeignKey(Other_Agencies, on_delete=models.CASCADE, blank=True, null=True)
    date_of_attack = models.DateTimeField()
    place_of_attack = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES,blank=True, null=True)
    number_of_TNFishermen_injured = models.PositiveIntegerField()
    number_of_TNFishermen_missing = models.PositiveIntegerField(blank=True, null=True)
    number_of_TNFishermen_died = models.PositiveIntegerField(blank=True, null=True)
    
    victim_names = models.CharField(max_length=200)
    attacker_details = models.CharField(max_length=200, blank=True, null=True)
    items_looted= models.CharField(max_length=200, blank=True, null=True)
    gist_of_attack = models.TextField()
    transfered_to = models.ForeignKey(PS, on_delete=models.SET_NULL, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.attacked_by} - {self.date_of_attack}"

class ArrestOfTNFishermen(models.Model):
    DISTRICT_CHOICES = [
        ('Chennai', 'Chennai'),
        ('Chengalpattu', 'Chengalpattu'),
        ('Villupuram', 'Villupuram'),
        ('Rameswaram', 'Rameswaram'),
        ('Cuddalore', 'Cuddalore'),
    ]

    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    date_of_arrest = models.DateTimeField()
    place_of_arrest = models.CharField(max_length=200)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES,blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    arrested_by = models.ForeignKey(Other_Agencies, on_delete=models.CASCADE, blank=True, null=True)
    number_of_TNFishermen_arrested = models.PositiveIntegerField()
    arrested_Fishermen_names = models.CharField(max_length=200)
    no_of_boats_seized = models.PositiveIntegerField(blank=True, null=True)
    boat_details = models.CharField(max_length=200, blank=True, null=True)
    gist_of_arrest = models.TextField()
    number_of_TNFishermen_released = models.PositiveIntegerField(blank=True, null=True)
    no_of_boats_released = models.PositiveIntegerField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.number_of_TNFishermen_arrested} - {self.date_of_arrest}"


class ArrestOfSLFishermen(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    date_of_arrest = models.DateTimeField()
    place_of_arrest = models.CharField(max_length=200)
    ps_limit = models.CharField(max_length=200)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    arrested_by = models.ForeignKey(Other_Agencies, on_delete=models.CASCADE, blank=True, null=True)
    number_of_SLFishermen_arrested = models.PositiveIntegerField()
    arrested_Fishermen_name = models.CharField(max_length=200)
    no_of_boats_seized = models.PositiveIntegerField(blank=True, null=True)
    boat_details = models.CharField(max_length=200, blank=True, null=True)
    gist_of_arrest = models.TextField()
    number_of_SLFishermen_released = models.PositiveIntegerField(blank=True, null=True)
    no_of_boats_released = models.PositiveIntegerField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.number_of_SLFishermen_arrested} - {self.date_of_arrest}"

class OnRoadVehicleStatus(models.Model):
    VEHICLE_TYPE_CHOICES = [('TWO_WHEELER', 'Two Wheeler'),('FOUR_WHEELER', 'Four Wheeler'),('ATV', 'ATV'),]
    WORKING_STATUS_CHOICES = [('WORKING', 'Working'),('NOT_WORKING', 'Not Working'),('CONDEMNED', 'Condemned'),('Other', 'Other')]
    
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    vehicle_number = models.CharField(max_length=100, unique=True)
    working_status = models.CharField(max_length=20, choices=WORKING_STATUS_CHOICES)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    alloted_to =  models.CharField(max_length=100,  null=True, blank=True,default="-")
    remarks = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_vehicle_type_display()} - {self.vehicle_number}"

class OnWaterVehicleStatus(models.Model):
    BOAT_TYPE_CHOICES = [('12_TON_BOAT', '12 Ton Boat'),('5_TON_BOAT', '5 Ton Boat'),('JET_SKI', 'Jet Ski'),('JET_BOAT', 'Jet Boat'),('AMPHIBIOUS_CRAFT', 'Amphibious Craft')]
    WORKING_STATUS_CHOICES = [('WORKING', 'Working'), ('NOT_WORKING', 'Not Working'), ('CONDEMNED', 'Condemned'),('Other', 'Other')]
    
    boat_type = models.CharField(max_length=50, choices=BOAT_TYPE_CHOICES)
    boat_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    working_status = models.CharField(max_length=20, choices=WORKING_STATUS_CHOICES)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.boat_type} - {self.boat_number}"
    
class VVCmeeting(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_vvc = models.DateField()
    village_name = models.CharField(max_length=200)
    number_of_villagers = models.PositiveIntegerField()
    conducted_by = models.CharField(max_length=200)
    vvc_image = models.ImageField(upload_to='vvc_images/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic'])])
    vvc_details = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_of_vvc} - {self.village_name} - {self.number_of_villagers} Villagers"

class BeatDetails(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_beat = models.DateField()
    day_beat_count = models.IntegerField(default=0)
    night_beat_count = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mps_limit} - {self.date_of_beat}"

class Proforma(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    date_of_proforma = models.DateField()
    officer=models.ForeignKey('Officer', on_delete=models.CASCADE,null=True, blank=True)

    mps_visited = models.IntegerField(default=0)
    check_post_checked = models.IntegerField(default=0)
    boat_guard_checked = models.IntegerField(default=0)
    vvc_meeting_conducted = models.IntegerField(default=0)
    villages_visited = models.IntegerField(default=0)
    meetings_attended = models.IntegerField(default=0)
    awareness_programs_conducted = models.IntegerField(default=0)
    coastal_security_exercises_conducted = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.date_of_proforma}"
    
class BoatPatrol(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    patrol_officer = models.ForeignKey('Officer', on_delete=models.CASCADE,null=True, blank=True)
    boat_type = models.CharField(max_length=50, choices=[('12_TON_BOAT', '12 Ton Boat'), ('5_TON_BOAT', '5 Ton Boat'), ('JET_SKI', 'Jet Ski'), ('JET_BOAT', 'Jet Boat'), ('AMPHIBIOUS_CRAFT', 'Amphibious Craft')])
    boat_number = models.ForeignKey(        'OnWaterVehicleStatus',on_delete=models.SET_NULL,null=True,blank=True)    
    date_of_patrol = models.DateField()
    patrol_start_time = models.TimeField()
    patrol_end_time = models.TimeField()
    patrol_place = models.CharField(max_length=200)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    numberof_boats_checked = models.PositiveIntegerField()
    registration_numberofboats_checked = models.TextField(max_length=200, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patrol_officer} - {self.mps_limit} - {self.date_of_patrol}"

class Atvpatrol(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    patrol_officer = models.CharField(max_length=200)
    atv_number = models.ForeignKey('OnRoadVehicleStatus',on_delete=models.SET_NULL,null=True,blank=True,limit_choices_to={'vehicle_type': 'ATV'},related_name='atv_patrols')
    date_of_patrol = models.DateField()
    patrol_start_time = models.TimeField()
    patrol_end_time = models.TimeField()
    patrol_place = models.CharField(max_length=200)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patrol_officer} - {self.atv_number} - {self.date_of_patrol}"

class VehicleCheckPost(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    officer = models.ForeignKey('Officer', on_delete=models.CASCADE,null=True, blank=True)
    date_of_check = models.DateField()
    vehicle_check_start_time = models.TimeField()
    vehicle_check_end_time = models.TimeField()
    check_post = models.ForeignKey('CheckPost', on_delete=models.CASCADE)  
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_vehicles_checked = models.PositiveIntegerField()
    registration_numbers  = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.check_post} - {self.mps_limit} - {self.date_of_check}"

class VehicleCheckothers(models.Model):
    user = models.ForeignKey('dsr.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    officer = models.ForeignKey('Officer', on_delete=models.CASCADE,null=True, blank=True)
    date_of_check = models.DateField()
    vehicle_check_start_time = models.TimeField()
    vehicle_check_end_time = models.TimeField()
    place_of_check = models.CharField(max_length=200)
    mps_limit = models.ForeignKey(MPS, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_vehicles_checked = models.PositiveIntegerField()
    registration_numbers = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vehicle Check by {self.officer} on {self.date_of_check}"
