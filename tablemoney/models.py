from django.db import models
from userprofile.models import UserProfile, Payee
from django.db.models.signals import pre_save, post_save, post_delete
from django.core.urlresolvers import reverse
# Create your models here.

MONTH_CHOICES = (
	('一月', '一月'),
	('二月', '二月'),
	('三月', '三月'),
	('四月', '四月'),
	('五月', '五月'),
	('六月', '六月'),
	('七月', '七月'),
	('八月', '八月'),
	('九月', '九月'),
	('十月', '十月'),
	('十一月', '十一月'),
	('十二月', '十二月'),
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

		self.month_total = 0
		prices = self.tablemoney_set.all()
		for p in prices:
			self.month_total += p.totle_price

		self.current_money = 0
		current = self.tablemoney_set.filter(pay_off=True)
		for c in current:
			self.current_money += c.totle_price
		self.save()

	def get_absolute_url(self):
		return reverse ('table_money_detail', kwargs={'pk':self.pk})

	class Meta:
		ordering = ['-pk']

	def remove(self):
		return '%s/?delete=True' %(self.pk)

def get_payer_post_save_receiver(sender, instance, *args, **kwargs):
	payers = UserProfile.objects.all()
	month = Month.objects.get(month=instance.month, year=instance.year)
	year = month.year
	for payer in payers:
		table_money, create = TableMoney.objects.get_or_create(name=payer, month=month, year=year)

post_save.connect(get_payer_post_save_receiver, sender=Month)



class TableMoney(models.Model):
	name = models.ForeignKey(UserProfile)
	month = models.ForeignKey(Month)
	year = models.PositiveIntegerField()
	day_price = models.IntegerField(null=True, blank=True)
	totle_price = models.IntegerField(default=1,null=True, blank=True)
	workday_count = models.PositiveIntegerField(default=0)
	pay_off = models.BooleanField(default=False)
	payee = models.ForeignKey(Payee, null=True, blank=True)
	pay_date = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
	note = models.CharField(max_length=20, blank=True)
	

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ['name']



def update_month_total_post_receiver(sender, instance, *args, **kwargs):
	instance.month.update_month_total()

post_save.connect(update_month_total_post_receiver, sender=TableMoney)
post_delete.connect(update_month_total_post_receiver, sender=TableMoney)



def get_price_pre_save_receiver(sender, instance, *args, **kwargs):
	if instance.name.rank == '隊員':
		instance.day_price = 110
	else:
		instance.day_price = 80
		instance.workday_count = 20
	day_price = instance.day_price
	instance.totle_price = day_price * instance.workday_count

pre_save.connect(get_price_pre_save_receiver, sender=TableMoney)






