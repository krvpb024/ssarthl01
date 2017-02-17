from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
# Create your models here.

class ZhuDi(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class ZuXun(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

def upload_location(instance, filename):
	date = instance.date.split('.')[1] + instance.date.split('.')[2]

	return "{} {}/{}".format(date, instance.session, filename)

class ZhuDiTable(models.Model):
	session = models.ForeignKey(ZhuDi)
	date = models.CharField(max_length=20)
	img = models.FileField(upload_to=upload_location)
	img2 = models.FileField(upload_to=upload_location)
	img3 = models.FileField(upload_to=upload_location, blank=True)
	time_stamp = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-pk']

	def __str__(self):
		return self.date

	def get_absolute_url(self):
		return reverse ('zhudi_table_detail', kwargs={'pk':self.pk})

def delete_zhudi_post_save_receiver(sender, instance, *args, **kwargs):
	zhudis = ZhuDiTable.objects.all().order_by('pk')
	table_number = zhudis.count()
	while table_number >5:
		zhudis.first().delete()
		table_number = zhudis.count()

post_save.connect(delete_zhudi_post_save_receiver, sender=ZhuDiTable)

def upload_location_zuxun(instance, filename):

	date = instance.date.split('.')[1] + instance.date.split('.')[2]

	return "{} {}/{}".format(date, instance.session, filename)


class ZuXunTable(models.Model):
	session = models.CharField(max_length=50)
	date = models.CharField(max_length=20)
	img = models.FileField(upload_to=upload_location_zuxun)
	img2 = models.FileField(upload_to=upload_location_zuxun)
	img3 = models.FileField(upload_to=upload_location_zuxun, blank=True)

	class Meta:
		ordering = ['-pk']

	def __str__(self):
		return self.date

	def get_absolute_url(self):
		return reverse ('zuxun_table_detail', kwargs={'pk':self.pk})

def delete_zuxun_post_save_receiver(sender, instance, *args, **kwargs):
	zuxuns = ZuXunTable.objects.all().order_by('pk')
	table_number = zuxuns.count()
	while table_number >5:
		zuxuns.first().delete()
		table_number = zuxuns.count()

post_save.connect(delete_zuxun_post_save_receiver, sender=ZuXunTable)
