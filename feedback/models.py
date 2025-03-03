from django.db import models
from customers.models import Customer
from orders.models import Orders
# Create your models here.
class CustomerFeedback(models.Model):
    feedback_id = models.AutoField(db_column='Feedback_ID', primary_key=True)  # primary key field.
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, db_column='Order_ID', blank=True, null=True)  # # Unique order ID reference
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, db_column='Customer_ID', blank=True, null=True)  #Foreign key reference to Customer.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Rating field 
    feedback_date = models.DateField(auto_now_add=True, db_column='Feedback_Date') # Feedback date defaults to the current date
    class Meta:
        db_table = 'customer_feedback'
    
    def __str__(self):
        return f'Feedback {self.feedback_id} - Rating: {self.rating}'