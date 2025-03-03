from django.db import models

# Create your models here.
class Restaurant(models.Model):
    BRANCH_TYPE_CHOICES = [
        ('Main', 'Main'),
        ('Branch', 'Branch'),
    ]
    
    restaurant_id = models.AutoField(db_column='Restaurant_ID', primary_key=True) 
    name = models.CharField(db_column='Name', max_length=100) 
    street = models.CharField(db_column='Street', max_length=100, blank=True, null=True) 
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True) 
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True) 
    zip_code = models.CharField(db_column='Zip_Code', max_length=10, blank=True, null=True) 
    contact_no = models.CharField(db_column='Contact_No', unique=True, max_length=15) 
    branch_type = models.CharField(max_length=10, choices=BRANCH_TYPE_CHOICES, default='Main')
    

    class Meta:
        db_table = 'restaurant'
