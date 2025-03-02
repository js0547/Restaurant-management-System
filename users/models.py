from django.db import models
from restaurant.models import Restaurant
# Create your models here.
class User(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    restaurant = models.ForeignKey(Restaurant, models.DO_NOTHING, db_column='Restaurant_ID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=6)  # Field name made lowercase.
    access_level = models.CharField(db_column='Access_Level', max_length=9)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
