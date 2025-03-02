from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.AutoField(db_column='Restaurant_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zip_code = models.CharField(db_column='Zip_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contact_no = models.CharField(db_column='Contact_No', unique=True, max_length=15)  # Field name made lowercase.
    branch_type = models.CharField(db_column='Branch_Type', max_length=6)  # Field name made lowercase.
    branch_name = models.CharField(db_column='Branch_Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restaurant'
