from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete

# Create your models here.

RANK_CHOICES = (
	('隊員', '隊員'),
	('替代役', '替代役'),
)


class MemberManager(models.Manager):
	def get_queryset(self):
		return super(MemberManager, self).get_queryset().filter(rank='隊員')

class SubstituteManager(models.Manager):
	def get_queryset(self):
		return super(SubstituteManager, self).get_queryset().filter(rank='替代役')
class EatManager(models.Manager):
	def get_queryset(self):
		return super(EatManager, self).get_queryset().filter(eat=True)

class UserProfile(models.Model):
	name = models.CharField(max_length=20)
	rank = models.CharField(max_length=20, choices=RANK_CHOICES)
	number = models.IntegerField()
	mobile_phone = models.CharField(max_length=20, null=True, blank=True)
	home_phone = models.CharField(max_length=20, null=True, blank=True)
	emergency_call = models.CharField(max_length=20, null=True, blank=True)
	eat = models.BooleanField(default=True)

	objects = models.Manager()
	members = MemberManager()
	substitutes = SubstituteManager()
	eats = EatManager()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['number']

	def remove(self):
		return '?pk=%s&delete=True' %(self.pk)

def create_payee_post_save_receiver(sender, instance, created, *args, **kwargs):

	if created:
		if instance.rank == "替代役":
			new_payee, create = Payee.objects.get_or_create(name=instance.name, identity=instance.pk)
	try:
		payee = Payee.objects.get(identity=instance.pk)
		payee.name = instance.name
		payee.save()
	except:
		pass

post_save.connect(create_payee_post_save_receiver, sender=UserProfile)

def delete_payee_post_delete_receiver(sender, instance, *args, **kwargs):


		try:
			payee = Payee.objects.get(identity=instance.pk)
			payee.delete()
		except:
			pass

post_delete.connect(delete_payee_post_delete_receiver, sender=UserProfile)

class Payee(models.Model):
	name = models.CharField(max_length=20)
	identity = models.IntegerField()

	def __str__(self):
		return self.name
