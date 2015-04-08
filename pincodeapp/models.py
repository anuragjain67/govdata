from django.db import models

# Create your models here.


class PinCodeDirectory(models.Model):
    office_name = models.CharField(max_length=128, null=True)
    pincode = models.IntegerField(unique=True, db_index=True)
    office_type = models.CharField(max_length=10, null=True)
    delivery_status = models.CharField(max_length=20, null=True)
    division_name = models.CharField(max_length=50, null=True)
    region_name = models.CharField(max_length=50, null=True, db_index=True)
    circle_name = models.CharField(max_length=50, null=True, db_index=True)
    taluk = models.CharField(max_length=50, null=True)
    district_name = models.CharField(max_length=50, null=True, db_index=True)
    state_name = models.CharField(max_length=50, null=True, db_index=True)