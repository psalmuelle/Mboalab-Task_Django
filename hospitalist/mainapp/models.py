from django.db import models
from django.contrib.auth.models import User


class HospitalDetail(models.Model):


    class OwnershipChoice(models.TextChoices):
        NONE = 'None'
        PRIVATE = 'Private'
        PUBLIC = 'Public'
        NON_PROFIT = 'Non-Profit'

    class FacilityLevelChoice(models.TextChoices):
        NONE = 'None'
        PRIMARY = 'Primary'
        SECONDARY = 'Secondary'
        TETIARY = 'Tetiary'

    class FacilityTypeChoice(models.TextChoices):
        NONE = 'None'
        GENERAL = 'General'
        SPECIALIST = 'Specialist'
        TEACHING = 'Teaching'


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    hospital_name = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    website_url = models.URLField(null=True)
    email = models.EmailField(null=True)
    hotline = models.CharField(max_length=15, null=True)
    operating_hours = models.CharField(max_length=50, null=True)
    ownership = models.CharField(max_length=50, choices= OwnershipChoice.choices, default=OwnershipChoice.NONE)
    facility_level = models.CharField(max_length=50, choices= FacilityLevelChoice.choices, default=FacilityLevelChoice.NONE)
    facility_type = models.CharField(max_length=15, choices= FacilityTypeChoice.choices, default= FacilityTypeChoice.NONE)
    services_offered = models.CharField(max_length=30000, blank=True, null=True)
    bed_spaces = models.IntegerField(default=0)
    other_facilities= models.CharField(max_length=30000, blank=True, null=True)
