from django import forms
from django.forms.models import modelformset_factory

from .models import Month, TableMoney


class MonthCreateForm(forms.ModelForm):

	class Meta:
		model = Month

		fields = [
		'month',
		'year',
		]
		labels = {
        'month': '月份',
        'year': '年份',
        }
	def __init__(self, *args, **kwargs):
		super(MonthCreateForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.error_messages = {
			'required':'請填入{fieldname}'.format(fieldname=field.label),
			'unique':"此月份表格已存在",

			}


class WorkDayForm(forms.ModelForm):

	class Meta:
		model = TableMoney

		fields = [
		'workday_count',
		]


WorkDayFormSet = modelformset_factory(TableMoney, form=WorkDayForm, extra=0)


class TableMoneyPayForm(forms.ModelForm):

	class Meta:
		model = TableMoney

		fields = [
		'pay_off',
		'payee',
		'note',
		]


TableMoneyPayFormSet = modelformset_factory(TableMoney, form=TableMoneyPayForm, extra=0)























