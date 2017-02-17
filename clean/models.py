from django.db import models
from userprofile.models import UserProfile
from holiday.models import Holiday, Date
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
import datetime
import calendar
import random

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

class CleanMonth(models.Model):
	year = models.PositiveIntegerField()
	month = models.CharField(max_length=20, choices=MONTH_CHOICES)
	identify = models.CharField(max_length=20, null=True, blank=True)
	clean_dict = models.CharField(max_length=1000)

	def __str__(self):
		return self.month


def clean_month_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.identify = str(instance.year)+str(instance.month)

	holiday = Holiday.objects.filter(identify=instance.identify, name__rank='替代役')
	

	substitutes = UserProfile.substitutes.all()
	
	
	# 替代役編號list
	number_list = list(range(1, len(substitutes)+1))
	print(number_list)
	

	# 人員的放假日期
	holiday_list = []
	for h in holiday:
		holiday_list.append(h.date.all())
	

	# 所有天數
	foreignkkey_date_list = Date.objects.all()

	# 用來裝日期+O的列表 例如[1, O, O, 4, 5] 表示2跟3放假
	d_list = []

	for f in holiday_list:
		for date in foreignkkey_date_list:
		
			if date in f:
				d_list.append('O')
			else:
				d_list.append('n')


	# 用來將整個list以固定數量分割成更小的list的功能
	def chunks(l, n):
		for i in range(0, len(l), n):
			yield l[i:i + n]

	# 分隔好的list 每31個就分割一個 31是以日期列表的長度來定義 foreignkkey_date_list
	final_holiday_list = list(chunks((d_list),len(foreignkkey_date_list)))
	print(final_holiday_list)
	

	# 日期
	date_list = []
	date = datetime.datetime(int(instance.year)+1911, int(instance.month), 1)
	date_list.append(date.strftime('%d'))
	numdays = int(calendar.monthrange(int(instance.year)+1911, int(instance.month))[1])-1
	for i in range(numdays): 
		date += datetime.timedelta(days=1)
		date_list.append(date.strftime('%d'))
	
	people_holiday_list = []
	for day in final_holiday_list:
		people_holiday_list.append(day)
	print(people_holiday_list)

	# 讓zip出來的不是tuple
	list_each_holiday = [list(a) for a in zip(*people_holiday_list)]
	print(list_each_holiday)

	# 製作以日期為單位的打掃list
	dict_each_holiday = {}
	day = 1
	for each_holiday in list_each_holiday:
		if day <= len(date_list):
			dict_each_holiday[day] = each_holiday
			day += 1

	print(dict_each_holiday)

	seven = ['1', '2', '3', '4', '5', '幫忙', '幫忙']
	six = ['1', '2', '3', '4', '5', '幫忙']
	five = ['1', '2', '3', '4', '5']
	four = ['1', '2', '3', '4']
	three = ['1', '2', '3、4']
	two = ['1、3、4', '2']

	for each_day in dict_each_holiday:
		print(dict_each_holiday[each_day])
		for num, item in enumerate(dict_each_holiday[each_day]):
			if item == 'n':
				if len(substitutes) - dict_each_holiday[each_day].count('O') == 7:
					choice = random.choice(seven)
					while choice in dict_each_holiday[each_day]:
						choice = random.choice(seven)
					dict_each_holiday[each_day][num] = choice

				elif len(substitutes) - dict_each_holiday[each_day].count('O') == 6:
					choice = random.choice(six)
					while choice in dict_each_holiday[each_day]:
						choice = random.choice(six)
					dict_each_holiday[each_day][num] = choice

				elif len(substitutes) - dict_each_holiday[each_day].count('O') == 5:
					choice = random.choice(five)
					while choice in dict_each_holiday[each_day]:
						choice = random.choice(five)
					dict_each_holiday[each_day][num] = choice

				elif len(substitutes) - dict_each_holiday[each_day].count('O') == 4:
					choice = random.choice(four)
					while choice in dict_each_holiday[each_day]:
						choice = random.choice(four)
					dict_each_holiday[each_day][num] = choice
					
				elif len(substitutes) - dict_each_holiday[each_day].count('O') == 3:
					choice = random.choice(three)
					while choice in dict_each_holiday[each_day]:
						choice = random.choice(three)
					dict_each_holiday[each_day][num] = choice
					
				elif len(substitutes) - dict_each_holiday[each_day].count('O') == 2:
					choice = random.choice(two)
					while choice in dict_each_holiday[each_day]:
						choice = random.choice(two)
					dict_each_holiday[each_day][num] = choice
					

	print(dict_each_holiday)


	
pre_save.connect(clean_month_pre_save_receiver, sender=CleanMonth)

