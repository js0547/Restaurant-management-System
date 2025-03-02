from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(db_column='Customer_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'