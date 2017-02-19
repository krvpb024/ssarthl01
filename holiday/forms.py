from django import forms

from django.forms.models import modelformset_factory
from .models import HolidayMonth, Holiday, Date, HolidayMonthFromDocx

from django.utils.translation import ugettext_lazy as _


class HolidayMonthFromDocxForm(forms.ModelForm):

	class Meta:
		model = HolidayMonthFromDocx

		fields = [
		'year',
		'month',
		'holiday_file',
		]

		labels = {
		'year': '年份',
		'month': '月份',
		'holiday_file': '輪休表',
		}


class HolidayMonthCreateForm(forms.ModelForm):

	class Meta:
		model = HolidayMonth

		fields = [
		'year',
		'month',
		'holiday_count',
		]

		labels = {
		'year': _('年份'),
		'month': _('月份'),
		'holiday_count': _('本月假日'),
		}
		error_messages = {
		'year': {'required': _("請填入年份"),},
		'month': {'required': _("請填入月份"),},
		'holiday_count': {'required': _("請填入本月假日天數"),},
		}



class HolidayEditForm(forms.ModelForm):

	date = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Date.objects.all(), required=False)
	class Meta:
		model = Holiday

		fields = [
		'name',
		'date',
		'holiday_count',
		]
		labels = {
		'name': _('姓名'),
		'date': _('休假日期'),
		'holiday_count': _('本月假日'),
		}


	def clean(self):
		cleaned_data = super(HolidayEditForm, self).clean()
		date = cleaned_data.get("date")
		holiday_count = cleaned_data.get("holiday_count")
		if date.count() > holiday_count:
			raise forms.ValidationError('選取天數大於本於假日')

HolidayEditFormSet = modelformset_factory(Holiday, form=HolidayEditForm, extra=0)
