from django.db import models
from tablemoney.models import Month
from userprofile.models import UserProfile

# Create your models here.

class HolidayMonth(models.Model):
	year = models.PositiveIntegerField()
	month = models.ForeignKey(Month)
	name = models.ManyToManyField(UserProfile, through='Holiday')
	holiday_count = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.month

class Date(models.Model):
	date = models.CharField(max_length=20)
	def __str__(self):
		return self.date

class Holiday(models.Model):
	name = models.ForeignKey(UserProfile)
	year = models.PositiveIntegerField()
	month = models.ForeignKey(HolidayMonth)
	date = models.ManyToManyField(Date)
	work_day_count = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name
