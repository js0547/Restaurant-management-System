from django.db import models
from restaurant.models import Restaurant
# Create your models here.
class Staff(models.Model):
    staff_id = models.AutoField(db_column='Staff_ID', primary_key=True)  # Field name made lowercase.
    restaurant = models.ForeignKey(Restaurant, models.DO_NOTHING, db_column='Restaurant_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=7)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=10, decimal_places=2)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staff'