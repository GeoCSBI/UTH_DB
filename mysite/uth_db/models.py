from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):

	userName = models.CharField(max_length=40, null=False)
	firstName = models.CharField(max_length=40, null=False)
	lastName = models.CharField(max_length=40, null=False)
	password = models.CharField(max_length=12, null=False)
	madeReservation = models.IntegerField(default=0)
	type = models.CharField(max_length=40, null=False, default="plain")

	def __str__(self):
		return self.firstName + ' - ' + self.lastName