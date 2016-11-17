from django import forms
from django.forms.models import modelformset_factory

from .models import UserProfile

class CreateColleagueForm(forms.ModelForm):

	class Meta:
		model = UserProfile

		fields = [
		'name',
		'rank',
		'number',
		'mobile_phone',
		'home_phone',
		'emergency_call',
		]

        
		labels = {
        'name': '姓名',
        'rank': '身分',
        'number': '編號',
        'mobile_phone': '行動電話',
        'home_phone':'住宅電話',
        'emergency_call':'緊急聯絡人',
        }
	def __init__(self, *args, **kwargs):
		super(CreateColleagueForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.error_messages = {
			'required':'請填入{fieldname}'.format(fieldname=field.label),
			}
CreateColleagueFormSet = modelformset_factory(UserProfile, form=CreateColleagueForm, extra=0)


class EditNumberForm(forms.ModelForm):

	class Meta:
		model = UserProfile

		fields = [
		'number',
		'name',
		]

		labels = {
        'name': '姓名',
        'number': '編號',
        }



EditNumberFormSet = modelformset_factory(UserProfile, form=EditNumberForm, extra=0)