from django.db import models
from customers.models import Customer
# Create your models here.
class CustomerFeedback(models.Model):
    feedback_id = models.AutoField(db_column='Feedback_ID', primary_key=True)  # Field name made lowercase.
    order = models.OneToOneField('Orders', models.DO_NOTHING, db_column='Order_ID', blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_ID', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    feedback_date = models.DateField(db_column='Feedback_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_feedback'