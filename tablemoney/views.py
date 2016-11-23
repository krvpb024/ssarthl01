from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from userprofile.models import UserProfile
from .models import TableMoney, Month
from .forms import MonthCreateForm, WorkDayFormSet, TableMoneyPayFormSet
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.

def table_money_list(request):
	months = Month.objects.all()

	if request.method == 'GET':
		creat_month = request.GET.get('try_create')
		if creat_month:
			messages.add_message(request, messages.INFO, 'ss')
			return HttpResponseRedirect(reverse("holiday_list"))
	
	context = {
		'months':months,
	}
	return render(request, 'table_money_list.html', context)

def table_money_detail(request, pk):
	from holiday.models import HolidayMonth
	months = get_object_or_404(Month, pk=pk)
	table_moneys = months.tablemoney_set.all()
	holiday = get_object_or_404(HolidayMonth, month=months.month, year=months.year)
	

	if request.method == 'GET':
		delete_month = request.GET.get('delete')
		if delete_month:
			months.delete()
			return HttpResponseRedirect('/tablemoney/')

	context = {
		'months':months,
		'table_moneys':table_moneys,
		'holiday':holiday,
	}

	

	return render(request, 'table_money_detail.html', context)

def delete(request):
	c = TableMoney.objects.all()
	print(c)
	c.delete()
	

	return HttpResponseRedirect('/tablemoney/')

# def month_create(request):
# 	form = MonthCreateForm()

# 	# old_month = Month.objects.all()
# 	# if old_month.count() > 10:
# 	# 	Month.objects.all().order_by("pk")[0].delete()

# 	if request.method == 'POST':
# 		form = MonthCreateForm(request.POST)
# 		if form.is_valid():
# 			month = form.cleaned_data['month']
# 			year = form.cleaned_data['year']
# 			if Month.objects.filter(month=month, year=year):
# 				messages.add_message(request, messages.INFO, '此月份表格已製作')
# 			else:
# 				new_month = form.save()
# 				new_month.get_payer()

# 			return HttpResponseRedirect('/tablemoney/' + str(new_month.pk))

# 	return render(request, 'table_money_create.html', {'form': form})



def table_money_pay(request, pk):
	months = get_object_or_404(Month, pk=pk)
	table_moneys = months.tablemoney_set.all()
	formset = TableMoneyPayFormSet(queryset=table_moneys)

	if request.method =='POST':
		formset = TableMoneyPayFormSet(request.POST)
		
		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				form.save()
			return HttpResponseRedirect('/tablemoney/' + str(months.pk))

	context = {
	'formset': formset,
	'months': months
	}
	return render(request, 'table_money_pay.html', context)
