from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):

	dateBooked = models.DateField(null=True)
	timeBooked = models.TimeField(null=True)
	bookedBy = models.OneToOneField(User, null=False, default=0)
	persons = models.IntegerField(null=True)

	def __str__(self):
		return 'Date: {} | Time: {} | UserID: {}' .format(self.dateBooked, self.timeBooked, self.bookedBy)

class Table(models.Model):

	seats = models.IntegerField(default=4 ,null=False)
	isBooked = models.BooleanField(default=False, null=False)
	booking = models.ForeignKey(Booking, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return 'Tablbe id - {} : Seats - {} : IsBooked - {}'.format(self.id, self.seats, self.isBooked) 

	def setFree(self):

		if self.booking == models.null:
			self.isBooked = False


class Order(models.Model):

	tableOrdered = models.ForeignKey(Table, default=0)
	
	def __str__(self):
		return self.id


class Food(models.Model):

	foodName = models.CharField(max_length=40, null=False)
	foodCost = models.IntegerField(default=5,null=False)
	quantity = models.IntegerField(null=False, default=0)

	def __str__(self):
		return self.foodName

class FoodOrdered(models.Model):

	orderId = models.ForeignKey(Order)
	foodOrdered = models.ForeignKey(Food)
	quantity = models.IntegerField(null=True)