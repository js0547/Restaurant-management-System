from django.contrib import admin

# Register your models here.
from .models import Orders, OrderDetails

admin.site.register(Orders)
admin.site.register(OrderDetails)