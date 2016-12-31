from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Tables(models.Model):

	seats = models.IntegerField(default=4 ,null=False)
	isBooked = models.BooleanField(default=False, null=False)

	def __str__(self):
		return 'Tablbe id - {} : Seats - {}'.format(self.id, self.seats) 

class Menu(models.Model):

	foodName = models.CharField(max_length=40, null=False)
	foodCost = models.IntegerField(default=5,null=False)

	def __str__(self):
		return self.foodName