from django.db import models
from userprofile.models import UserProfile
from django.db.models.signals import pre_save, post_save, post_delete
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect


# Create your models here.

MONTH_CHOICES = (
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', '9'),
	('10', '10'),
	('11', '11'),
	('12', '12'),
)

class HolidayMonth(models.Model):
	year = models.PositiveIntegerField()
	month = models.CharField(max_length=20, choices=MONTH_CHOICES)
	name = models.ManyToManyField(UserProfile, through='Holiday')
	holiday_count = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.month
		
	def get_absolute_url(self):
		return reverse ('holiday_detail', kwargs={'pk':self.pk})

	def get_name(self):
		names = UserProfile.objects.all()
		month = HolidayMonth.objects.get(month=self.month, year=self.year)
		year = month.year
		for name in names:
			holiday, create = Holiday.objects.get_or_create(name=name, month=month, year=year)
			holiday.save()

	def remove(self):
		return '%s/?delete=True' %(self.pk)




class Date(models.Model):
	date = models.CharField(max_length=20)
	def __str__(self):
		return self.date

class Holiday(models.Model):
	name = models.ForeignKey(UserProfile)
	year = models.PositiveIntegerField()
	month = models.ForeignKey(HolidayMonth)
	date = models.ManyToManyField(Date, blank=True)
	work_day_count = models.CharField(max_length=20, default='尚未排假')
	identify = models.CharField(max_length=20)

	def __str__(self):
		return str(self.name)

def get_work_day_count_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.identify = str(instance.year)+str(instance.month)
	
pre_save.connect(get_work_day_count_pre_save_receiver, sender=Holiday)



def update_table_money_workday_count_post_save_receiver(sender, instance, *args, **kwargs):
	from tablemoney.models import TableMoney
	try:
		tablemoney = get_object_or_404(TableMoney, name=instance.name, year=instance.year, identify=instance.identify)
		tablemoney.save()
	except:
		pass

post_save.connect(update_table_money_workday_count_post_save_receiver, sender=Holiday)







