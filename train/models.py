from django.db import models
from django.core.urlresolvers import reverse
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
	month = instance.date.split('/')[0]
	date = instance.date.replace("/", "")
	return "{}月/{} {}/{}".format(month, date, instance.session, filename)

class ZhuDiTable(models.Model):
	session = models.ForeignKey(ZhuDi)
	date = models.CharField(max_length=20)
	img = models.FileField(upload_to=upload_location)
	img2 = models.FileField(upload_to=upload_location)
	img3 = models.FileField(upload_to=upload_location, blank=True)

	
	def __str__(self):
		return self.date
		
	def get_absolute_url(self):
		return reverse ('zhudi_table_detail', kwargs={'pk':self.pk})

class ZuXunTable(models.Model):
	session = models.ManyToManyField(ZuXun)
	date = models.CharField(max_length=20)
	img = models.FileField()
	
	def __str__(self):
		return self.date