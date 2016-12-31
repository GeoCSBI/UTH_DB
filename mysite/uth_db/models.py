from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Table(models.Model):

	seats = models.IntegerField(default=4 ,null=False)
	isBooked = models.BooleanField(default=False, null=False)
	dateBooked = models.DateField(null=True)
	timeBooked = models.TimeField(null=True)

	def __str__(self):
		return 'Tablbe id - {} : Seats - {}'.format(self.id, self.seats) 

class Order(models.Model):

	tableId = models.ForeignKey(Table, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.id

class Food(models.Model):

	foodName = models.CharField(max_length=40, null=False)
	foodCost = models.IntegerField(default=5,null=False)
	order = models.ForeignKey(Order, null=True)

	def __str__(self):
		return self.foodName

