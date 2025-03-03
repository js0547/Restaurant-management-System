from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(db_column='Customer_ID', primary_key=True)  # Primary key field
    name = models.CharField(db_column='Name', max_length=100)  #  Name field 
    phone_number = models.CharField(db_column='Phone_Number', max_length=15, blank=True, null=True)  # Phone number field, optional
    email = models.CharField(db_column='Email', unique=True, max_length=100, blank=True, null=True)  # Email field with Unique constraint

    class Meta:
        db_table = 'Customer'  # Specifies the database table name
        ordering = ['name']  # Orders records by name alphabetically
        
    def __str__(self):
        # Returns the name when the object is represented as a string
        return self.name