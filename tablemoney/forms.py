from django import forms
from django.forms.models import modelformset_factory

from .models import Month, TableMoney, ExtraTableMoney


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
		'pay_date',
		'note',
		]


TableMoneyPayFormSet = modelformset_factory(TableMoney, form=TableMoneyPayForm, extra=0)



class ExtraTableMoneyForm(forms.ModelForm):

	class Meta:
		model = ExtraTableMoney

		fields = [
		'name',
		'extra_price',
		]

		labels = {
		'name': '姓名',
		'extra_price': '金額',
		}

class ExtraTableMoneyPayForm(forms.ModelForm):

	class Meta:
		model = ExtraTableMoney

		fields = [
		'pay_off',
		'payee',
		'pay_date',
		'note',
		]
ExtraTableMoneyPayFormSet = modelformset_factory(ExtraTableMoney, form=ExtraTableMoneyPayForm, extra=0)
