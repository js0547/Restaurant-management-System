# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(db_column='Customer_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerFeedback(models.Model):
    feedback_id = models.AutoField(db_column='Feedback_ID', primary_key=True)  # Field name made lowercase.
    order = models.OneToOneField('Orders', models.DO_NOTHING, db_column='Order_ID', blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_ID', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    feedback_date = models.DateField(db_column='Feedback_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_feedback'


class Menu(models.Model):
    menu_id = models.AutoField(db_column='Menu_ID', primary_key=True)  # Field name made lowercase.
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='Restaurant_ID', blank=True, null=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='Item_Name', max_length=100)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'


class OrderDetails(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, db_column='Order_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Order_ID, Menu_ID) found, that is not supported. The first column is selected.
    menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='Menu_ID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    special_requests = models.TextField(db_column='Special_Requests', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_details'
        unique_together = (('order', 'menu'),)


class Orders(models.Model):
    order_id = models.AutoField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_ID', blank=True, null=True)  # Field name made lowercase.
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='Restaurant_ID', blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateTimeField(db_column='Order_Date', blank=True, null=True)  # Field name made lowercase.
    total_amount = models.DecimalField(db_column='Total_Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Payment(models.Model):
    payment_id = models.AutoField(db_column='Payment_ID', primary_key=True)  # Field name made lowercase.
    order = models.OneToOneField(Orders, models.DO_NOTHING, db_column='Order_ID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment_Method', max_length=11, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Restaurant(models.Model):
    restaurant_id = models.AutoField(db_column='Restaurant_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zip_code = models.CharField(db_column='Zip_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contact_no = models.CharField(db_column='Contact_No', unique=True, max_length=15)  # Field name made lowercase.
    branch_type = models.CharField(db_column='Branch_Type', max_length=6)  # Field name made lowercase.
    branch_name = models.CharField(db_column='Branch_Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restaurant'


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
