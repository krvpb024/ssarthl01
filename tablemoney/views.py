from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from userprofile.models import UserProfile
from .models import TableMoney, Month, ExtraTableMoney
from .forms import MonthCreateForm, WorkDayFormSet, TableMoneyPayFormSet, ExtraTableMoneyForm, ExtraTableMoneyPayFormSet
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
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

@login_required
def table_money_detail(request, pk):
	from holiday.models import HolidayMonth
	months = get_object_or_404(Month, pk=pk)
	table_moneys = months.tablemoney_set.all()
	holiday = get_object_or_404(HolidayMonth, month=months.month, year=months.year)
	extra_table_moneys = ExtraTableMoney.objects.filter(identify=str(months.year)+str(months.month))


	# if request.method == 'GET':
	# 	delete_month = request.GET.get('delete')
	# 	if delete_month:
	# 		months.delete()
	# 		return HttpResponseRedirect('/tablemoney/')

	context = {
		'months':months,
		'table_moneys':table_moneys,
		'holiday':holiday,
		'extra_table_moneys': extra_table_moneys
	}



	return render(request, 'table_money_detail.html', context)

@login_required
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

@login_required
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
			messages.add_message(request, messages.INFO, '繳費完成')
			return HttpResponseRedirect('/tablemoney/' + str(months.pk))

	context = {
	'formset': formset,
	'months': months
	}
	return render(request, 'table_money_pay.html', context)


@login_required
def extra_table_money_pay(request, pk):
	months = get_object_or_404(Month, pk=pk)
	extra_table_moneys = ExtraTableMoney.objects.filter(identify=str(months.year)+str(months.month))
	formset = ExtraTableMoneyPayFormSet(queryset=extra_table_moneys)

	if request.method =='POST':
		formset = ExtraTableMoneyPayFormSet(request.POST)

		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				form.save()
			messages.add_message(request, messages.INFO, '繳費完成')
			return HttpResponseRedirect('/tablemoney/' + str(months.pk))

	context = {
	'formset': formset,
	'months': months
	}
	return render(request, 'extra_table_money_pay.html', context)

@login_required
def add_extra_table_money(request, pk):
	form = ExtraTableMoneyForm()
	months = get_object_or_404(Month, pk=pk)

	if request.method == 'POST':
		form = ExtraTableMoneyForm(request.POST)
		if form.is_valid():
			extra = form.save(commit=False)
			extra.month = months
			extra.year = months.year
			extra.save()

			messages.add_message(request, messages.INFO, '項目新增完成')
			return HttpResponseRedirect('/tablemoney/' + str(months.pk))

	context = {
		'form': form,
		'months': months,
	}

	return render(request, 'add_extra_table_money.html', context)

def delete_extra_table_money_list(request, pk):
	month = get_object_or_404(Month, pk=pk)
	extra_table_moneys = ExtraTableMoney.objects.filter(identify=str(month.year)+str(month.month))

	if request.method == 'GET':
		delete_pk = request.GET.get('pk')
		delete_extra_table_money = request.GET.get('delete')

		if delete_extra_table_money:
			ExtraTableMoney.objects.filter(pk=delete_pk).delete()
			messages.add_message(request, messages.INFO, '已刪除繳費項目')
			return HttpResponseRedirect(reverse(table_money_detail, kwargs={"pk":pk}))
	context = {
		'month':month,
		'extra_table_moneys':extra_table_moneys,
	}

	return render(request, 'delete_extra_table_money.html', context)
