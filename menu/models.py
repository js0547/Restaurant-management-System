from django.db import models
from restaurant.models import Restaurant
# Create your models here.

class Menu(models.Model):
    menu_id = models.AutoField(db_column='Menu_ID', primary_key=True)  # Field name made lowercase.
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='Restaurant_ID', blank=True, null=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='Item_Name', max_length=100)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'