from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
import os
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

	return "{}/{}".format('zhudi', filename)

class ZhuDiTable(models.Model):
	session = models.ForeignKey(ZhuDi)
	date = models.CharField(max_length=20)
	img = models.FileField(upload_to=upload_location)
	img2 = models.FileField(upload_to=upload_location)
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

def delete_zhudi_file_post_delete_receiver(sender, instance, *args, **kwargs):
	if instance.img:
		try:
			if os.path.isfile(instance.img.path):
				os.remove(instance.img.path)
		except:
			pass
	if instance.img2:
		try:
			if os.path.isfile(instance.img2.path):
				os.remove(instance.img2.path)
		except:
			pass

post_delete.connect(delete_zhudi_file_post_delete_receiver, sender=ZhuDiTable)

def upload_location_zuxun(instance, filename):

	date = instance.date.split('.')[1] + instance.date.split('.')[2]

	return "{}/{}".format('zuxun', filename)


class ZuXunTable(models.Model):
	session = models.CharField(max_length=50)
	date = models.CharField(max_length=20)
	img = models.FileField(upload_to=upload_location_zuxun)
	img2 = models.FileField(upload_to=upload_location_zuxun)

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

def delete_zuxun_file_post_delete_receiver(sender, instance, *args, **kwargs):
	if instance.img:
		if os.path.isfile(instance.img.path):
			os.remove(instance.img.path)
	if instance.img2:
		if os.path.isfile(instance.img2.path):
			os.remove(instance.img2.path)

post_delete.connect(delete_zuxun_file_post_delete_receiver, sender=ZuXunTable)
