from django.db import models
from userprofile.models import UserProfile, Payee

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

class Month(models.Model):
	month = models.CharField(max_length=20, choices=MONTH_CHOICES)
	year = models.PositiveIntegerField()
	month_total = models.IntegerField(default=0)
	name = models.ManyToManyField(UserProfile, through='TableMoney')
	current_money = models.IntegerField(default=0)

	def __str__(self):
		return str(self.month)


	def update_month_total(self):

		# 因為table_money沒儲存一次就會加一次，如果有4個人，就會變成總額*4
		# 所以每次都歸0，這樣即使加了4次，也只會使原本的總額
		self.month_total = 0
		prices = self.tablemoney_set.all()
		for p in prices:
			self.month_total += p.totle_price

		extra_table_money = ExtraTableMoney.objects.filter(identify=str(self.year)+str(self.month))


		for extra_price in extra_table_money:
			self.month_total += extra_price.extra_price
		self.save()


	def update_current_money(self):
		self.current_money = 0
		current = self.tablemoney_set.filter(pay_off=True)

		for c in current:
			self.current_money += c.totle_price

		current_extra_money = ExtraTableMoney.objects.filter(identify=str(self.year)+str(self.month), pay_off=True)
		for extra_price in current_extra_money:
			self.current_money += extra_price.extra_price

		self.save()

	def get_absolute_url(self):
		return reverse ('table_money_detail', kwargs={'pk':self.pk})

	class Meta:
		ordering = ['-pk']

	# def remove(self):
	# 	return '%s/?delete=True' %(self.pk)

	def try_create(self):
		return '/?try_create=True'

	# def get_payer(self):
	# 	payers = UserProfile.eats.all()
	# 	month = Month.objects.get(month=self.month, year=self.year)
	# 	year = month.year
	# 	for payer in payers:
	# 		table_money, create = TableMoney.objects.get_or_create(name=payer, month=month, year=year)


def get_payer_post_save_receiver(sender, instance, created, *args, **kwargs):
	if created:
		payers = UserProfile.eats.all()
		month = Month.objects.get(month=instance.month, year=instance.year)
		year = month.year
		for payer in payers:
			table_money, create = TableMoney.objects.get_or_create(name=payer, month=month, year=year)

post_save.connect(get_payer_post_save_receiver, sender=Month)


class ExtraTableMoney(models.Model):
	name = models.ForeignKey(UserProfile)
	month = models.ForeignKey(Month)
	year = models.PositiveIntegerField()
	extra_price = models.PositiveIntegerField()
	pay_off = models.BooleanField(default=False)
	payee = models.ForeignKey(Payee, null=True, blank=True)
	note = models.CharField(max_length=20, blank=True)
	pay_date = models.CharField(max_length=20, blank=True)
	identify = models.CharField(max_length=20, default=0)

	def __str__(self):
		return str(self.name)

	def remove(self):
		return '?pk=%s&delete=True' %(self.pk)

def extra_table_money_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.identify = str(instance.year)+str(instance.month)

pre_save.connect(extra_table_money_pre_save_receiver, sender=ExtraTableMoney)

def update_post_save_receiver(sender, instance, *args, **kwargs):
	instance.month.update_month_total()

post_save.connect(update_post_save_receiver, sender=ExtraTableMoney)

def update_post_delete_receiver(sender, instance, *args, **kwargs):
	instance.month.update_month_total()

post_delete.connect(update_post_delete_receiver, sender=ExtraTableMoney)

def update_extra_current_money_post_save_receiver(sender, instance, *args, **kwargs):
	instance.month.update_current_money()

post_save.connect(update_extra_current_money_post_save_receiver, sender=ExtraTableMoney)

def update_extra_current_money_post_delete_receiver(sender, instance, *args, **kwargs):
	instance.month.update_current_money()

post_delete.connect(update_extra_current_money_post_delete_receiver, sender=ExtraTableMoney)



class TableMoney(models.Model):
	name = models.ForeignKey(UserProfile)
	month = models.ForeignKey(Month)
	year = models.PositiveIntegerField()
	day_price = models.IntegerField(null=True, blank=True)
	totle_price = models.IntegerField(default=1,null=True, blank=True)
	workday_count = models.PositiveIntegerField(default=0)
	pay_off = models.BooleanField(default=False)
	payee = models.ForeignKey(Payee, null=True, blank=True)
	note = models.CharField(max_length=20, blank=True)
	pay_date = models.CharField(max_length=20, blank=True)
	identify = models.CharField(max_length=20)

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ['name']





def get_price_pre_save_receiver(sender, instance, *args, **kwargs):
	from holiday.models import Holiday, HolidayFromDocx
	instance.identify = str(instance.year)+str(instance.month)

	try:
		holiday = get_object_or_404(HolidayFromDocx, name=instance.name, year=instance.year, identify=instance.identify)

		if instance.name.rank == '隊員':
			if holiday.work_day_count == "":
				pass
			else:
				instance.workday_count = holiday.work_day_count
				instance.day_price = 110
				day_price = instance.day_price
				instance.totle_price = int(day_price) * int(instance.workday_count)
		else:
			instance.day_price = 80
			instance.workday_count = 20
			day_price = instance.day_price
			instance.totle_price = int(day_price) * int(instance.workday_count)
	except:
		if instance.name.rank == '隊員':
			instance.day_price = 110
			day_price = instance.day_price
			instance.totle_price = int(day_price) * int(instance.workday_count)
		else:
			instance.day_price = 80
			instance.workday_count = 20
			day_price = instance.day_price
			instance.totle_price = int(day_price) * int(instance.workday_count)


pre_save.connect(get_price_pre_save_receiver, sender=TableMoney)

def update_month_total_post_save_receiver(sender, instance, *args, **kwargs):
	instance.month.update_month_total()

post_save.connect(update_month_total_post_save_receiver, sender=TableMoney)

def update_current_money_post_save_receiver(sender, instance, *args, **kwargs):
	instance.month.update_current_money()

post_save.connect(update_current_money_post_save_receiver, sender=TableMoney)
