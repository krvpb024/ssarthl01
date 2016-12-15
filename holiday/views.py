from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from userprofile.models import UserProfile
from tablemoney.models import TableMoney, Month
from .models import HolidayMonth, Holiday , Date
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
import calendar
import locale
from itertools import product
from .forms import HolidayMonthCreateForm, HolidayEditFormSet

# Create your views here.

def holiday_list(request):
	holiday_months = HolidayMonth.objects.all()

	context = {
	'holiday_months':holiday_months
	}

	return render(request,'holiday_list.html' , context)

def holiday_detail(request, pk):
	holiday_months = get_object_or_404(HolidayMonth, pk=pk)
	holidays = Holiday.objects.filter(month=holiday_months)
	locale.setlocale(locale.LC_ALL, 'zh_CN')
	

	# 顯示星期
	weekday_list = []
	date = datetime.datetime(int(holiday_months.year)+1911, int(holiday_months.month), 1)
	weekday_list.append(date.strftime('%a'))
	numdays = int(calendar.monthrange(int(holiday_months.year)+1911, int(holiday_months.month))[1])-1
	for i in range(numdays): 
		date += datetime.timedelta(days=1)
		weekday_list.append(date.strftime('%a'))

	# 顯示日期
	date_list = []
	date = datetime.datetime(int(holiday_months.year)+1911, int(holiday_months.month), 1)
	date_list.append(date.strftime('%-d'))
	numdays = int(calendar.monthrange(int(holiday_months.year)+1911, int(holiday_months.month))[1])-1
	for i in range(numdays): 
		date += datetime.timedelta(days=1)
		date_list.append(date.strftime('%-d'))

	# 顯示日期+星期
	date_weekday_list = zip(date_list, weekday_list)

	# 人員的放假日期
	holiday_list = []
	for holiday in holidays:
		holiday_list.append(holiday.date.all())

	# 所有天數
	foreignkkey_date_list = Date.objects.all()

	# 用來裝日期+O的列表 例如[1, O, O, 4, 5] 表示2跟3放假
	d_list = []

	for f in holiday_list:
		for date in foreignkkey_date_list:
		
			if date in f:
				d_list.append('O')
			else:
				d_list.append('')

	# 用來將整個list以固定數量分割成更小的list的功能
	def chunks(l, n):
		for i in range(0, len(l), n):
			yield l[i:i + n]

	# 分隔好的list 每31個就分割一個 31是以日期列表的長度來定義 foreignkkey_date_list
	final_holiday_list = chunks((d_list),len(foreignkkey_date_list))
	final_holiday = zip(holidays, final_holiday_list)


	# 刪除表格
	# if request.method == 'GET':
	# 	delete_month = request.GET.get('delete')
	# 	if delete_month:
	# 		holiday_months.delete()
	# 		return HttpResponseRedirect(reverse("holiday_list"))

	if request.method == 'GET':
		delete_month = request.GET.get('delete')
		create_month = request.GET.get('create')
		month = request.GET.get('month')
		year = request.GET.get('year')
		if delete_month:
			holiday_months.delete()
			return HttpResponseRedirect(reverse("holiday_list"))
		if create_month:
			tablemoney_month, create = Month.objects.get_or_create(month=month, year=year)
			if create == False:
				return HttpResponseRedirect(tablemoney_month.get_absolute_url())
			else:
				messages.add_message(request, messages.INFO, '本月份餐費表格已重新製作')
				return HttpResponseRedirect(tablemoney_month.get_absolute_url())
			
	context = {
		'holiday_months':holiday_months,
		'holidays':holidays,
		'date_list':date_list,
		'weekday_list':weekday_list,
		'date_weekday_list':date_weekday_list,
		'final_holiday_list':final_holiday_list,
		'final_holiday':final_holiday,
		'test':2,
		
	}

	return render(request,'holiday_detail.html' , context)




def holiday_create(request):
	form = HolidayMonthCreateForm()

	if request.method == 'POST':
		form = HolidayMonthCreateForm(request.POST)
		if form.is_valid():
			month = form.cleaned_data['month']
			year = form.cleaned_data['year']
			if HolidayMonth.objects.filter(month=month, year=year):
				messages.add_message(request, messages.INFO, '此月份表格已製作')
			else:
				new_month = form.save()
				# new_month.get_name()
				messages.add_message(request, messages.INFO, '本月餐費表格同時製作完成')

				return HttpResponseRedirect('/holiday/' + str(new_month.pk))

	return render(request, 'holiday_month_create.html', {'form': form})


def edit_holiday(request, month_pk):
	holiday_months = get_object_or_404(HolidayMonth, pk=month_pk)
	name = holiday_months.holiday_set.all()
	holidays = Holiday.objects.filter(month=holiday_months)
	locale.setlocale(locale.LC_ALL, 'zh_CN')
	formset = HolidayEditFormSet(queryset=name)


	# 顯示星期
	weekday_list = []
	date = datetime.datetime(int(holiday_months.year)+1911, int(holiday_months.month), 1)
	weekday_list.append(date.strftime('%a'))
	numdays = int(calendar.monthrange(int(holiday_months.year)+1911, int(holiday_months.month))[1])-1
	for i in range(numdays): 
		date += datetime.timedelta(days=1)
		weekday_list.append(date.strftime('%a'))

	# 顯示日期
	date_list = []
	date = datetime.datetime(int(holiday_months.year)+1911, int(holiday_months.month), 1)
	date_list.append(date.strftime('%-d'))
	numdays = int(calendar.monthrange(int(holiday_months.year)+1911, int(holiday_months.month))[1])-1
	for i in range(numdays): 
		date += datetime.timedelta(days=1)
		date_list.append(date.strftime('%-d'))

	# 顯示日期+星期
	date_weekday_list = zip(date_list, weekday_list)

	# 人員的放假日期
	holiday_list = []
	for holiday in holidays:
		holiday_list.append(holiday.date.all())

	# 所有天數
	foreignkkey_date_list = Date.objects.all()

	# 用來裝日期+O的列表 例如[1, O, O, 4, 5] 表示2跟3放假
	d_list = []

	for f in holiday_list:
		for date in foreignkkey_date_list:
		
			if date in f:
				d_list.append('O')
			else:
				d_list.append('')

	# 用來將整個list以固定數量分割成更小的list的功能
	def chunks(l, n):
		for i in range(0, len(l), n):
			yield l[i:i + n]

	# 分隔好的list 每31個就分割一個 31是以日期列表的長度來定義 foreignkkey_date_list
	final_holiday_list = chunks((d_list),len(foreignkkey_date_list))
	final_holiday = zip(holidays, final_holiday_list)


	if request.method =='POST':
		formset = HolidayEditFormSet(request.POST)
		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				edit_holiday = form.save()
				edit_holiday.work_day_count = form.cleaned_data['date'].count()
				edit_holiday = form.save()
			messages.add_message(request, messages.INFO, '輪休表編輯完成')
			return HttpResponseRedirect('/holiday/' + str(holiday_months.pk))

	context = {
	'formset': formset,
	'holiday_months': holiday_months,
	'name': name,
	'date_list':date_list,
	'weekday_list':weekday_list,
	'date_weekday_list':date_weekday_list,
	'final_holiday_list':final_holiday_list,
	'final_holiday':final_holiday,
	}
	return render(request, 'edit_holiday.html', context)
