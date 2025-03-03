from django.db import models
from restaurant.models import Restaurant
# Create your models here.

class Menu(models.Model):
    menu_id = models.AutoField(db_column='Menu_ID', primary_key=True)  # Field name made lowercase.
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, db_column='Restaurant_ID', blank=True, null=True) # Foreign key reference to Restaurant.
    item_name = models.CharField(db_column='Item_Name',null=False, max_length=100)  # Item name
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, null=False)  # Price field
    CATEGORY_CHOICES = [
        ('Appetizer', 'Appetizer'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Beverage', 'Beverage'),
    ]
    category = models.CharField(db_column='Category',  choices=CATEGORY_CHOICES,max_length=20, blank=True, null=True) 

    class Meta:
        db_table = 'menu'
        
    
    def __str__(self):
        return f'{self.item_name} - {self.price}'