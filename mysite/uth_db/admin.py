from django.contrib import admin
from .models import Food, Table, Order, Booking
# Register your models here.

admin.site.register(Food)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Booking)