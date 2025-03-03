from django.db import models
from orders.models import Orders
# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(db_column='Payment_ID', primary_key=True)  # Field name made lowercase.
    order = models.OneToOneField(Orders, models.DO_NOTHING, db_column='Order_ID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment_Method', max_length=11, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'payment'