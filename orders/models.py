from django.db import models

# Create your models here.
class Orders(models.Model):
    order_id = models.AutoField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_ID', blank=True, null=True)  # Field name made lowercase.
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='Restaurant_ID', blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateTimeField(db_column='Order_Date', blank=True, null=True)  # Field name made lowercase.
    total_amount = models.DecimalField(db_column='Total_Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'
        

class OrderDetails(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, db_column='Order_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Order_ID, Menu_ID) found, that is not supported. The first column is selected.
    menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='Menu_ID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    special_requests = models.TextField(db_column='Special_Requests', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_details'
        unique_together = (('order', 'menu'),)