from django.db import models
from restaurant.models import Restaurant
from customers.models import Customer
from menu.models import Menu
from django.db.models import CheckConstraint, Q

# Create your models here.
class Orders(models.Model):
    order_id = models.AutoField(db_column='Order_ID', primary_key=True)  
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, db_column='Customer_ID', blank=True, null=True) # Foreign key reference to Customer
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, db_column='Restaurant_ID', blank=True, null=True)
    total_amount = models.DecimalField(db_column='Total_Amount', max_digits=10, decimal_places=2)  #  # Total amount
    order_date = models.DateTimeField(auto_now_add=True, db_column='Order_Date') #Order date 
    class Meta:
        db_table = 'orders'
    
    def __str__(self):
         return f'Order {self.order_id} - {self.total_amount}'

        

class OrderDetails(models.Model):
    order = models.OneToOneField(Orders, on_delete=models.CASCADE)     # Foreign key reference to Orders, deletes details if order is deleted
    menu = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.SET_NULL)  # Foreign key reference to Menu, deletes details if menu item is deleted
    quantity = models.IntegerField(null=False,db_column='Quantity')  # Field name made lowercase.
    special_requests = models.TextField(db_column='Special_Requests', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Order_Details'  # Specifies the database table name
        constraints = [
            CheckConstraint(check=Q(quantity__gt=0), name='quantity_greater_than_0')
            ]
        unique_together = ('order', 'menu')  # Composite primary key equivalent
    
    def __str__(self):
        return f'Order {self.order.order_id} - {self.menu.item_name} x {self.quantity}'