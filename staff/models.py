from django.db import models
from restaurant.models import Restaurant
# Create your models here.
class Staff(models.Model):
    ROLE_CHOICES = [
        ('Chef', 'Chef'),
        ('Waiter', 'Waiter'),
        ('Manager', 'Manager'),
        ('Janitor', 'Janitor'),
    ]
    
    staff_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

class Meta:
    db_table = 'staff' 
    
    def __str__(self):
        return f"{self.name} - {self.role}"
