from django import forms

from django.forms.models import modelformset_factory
from .models import HolidayMonth, Holiday, Date

from django.utils.translation import ugettext_lazy as _


class HolidayMonthCreateForm(forms.ModelForm):

	class Meta:
		model = HolidayMonth

		fields = [
		'year',
		'month',
		]

		labels = {
		'year': _('年份'),
		'month': _('月份'),
		}
		error_messages = {
		'year': {'required': _("請填入年份"),},
		'month': {'required': _("請填入月份"),},
		}


class HolidayEditForm(forms.ModelForm):

	date = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Date.objects.all())
	class Meta:
		model = Holiday

		fields = [
		'name',
		'date',
		]
		labels = {
		'name': _('名字'),
		'date': _('休假日期'),
		}

		def __init__(self, *args, **kwargs):
			super(HolidayEditForm, self).__init__(*args, **kwargs)
			for field in self.fields.values():
				field.error_messages = {
				'required':'請填入{fieldname}'.format(fieldname=field.label)
				}

# HolidayEditFormSet = modelformset_factory(Holiday, form=HolidayEditForm, extra=0)