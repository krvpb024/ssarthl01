from django import forms
from .models import ZhuDiTable, ZuXunTable, ZuXun, ZhuDi
from django.utils.translation import ugettext_lazy as _

class ZhuDiTableForm(forms.ModelForm):
	img = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	img3 = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

	class Meta:
		model = ZhuDiTable

		fields = [
			'session',
			'date',
			'img',
			'img3',
		]

		labels = {
			'session': _('項目'),
			'date': _('日期'),
			'img': _('表格照片'),
			'img3': _('其餘照片'),
		}

class ZuXunTableForm(forms.ModelForm):
	session = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=ZuXun.objects.all(), required=False)
	img = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	img3 = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

	class Meta:
		model = ZuXunTable

		fields = [
			'session',
			'date',
			'img',
			'img3',
		]

		labels = {
			'session': _('項目'),
			'date': _('日期'),
			'img': _('表格照片'),
			'img3': _('其餘照片'),
		}

class ZhuDiSessionForm(forms.ModelForm):

	class Meta:
		model = ZhuDi

		fields = [
			'name'
		]
		
		labels = {
			'name': _('項目'),

		}


class ZuXunSessionForm(forms.ModelForm):

	class Meta:
		model = ZuXun

		fields = [
			'name'
		]
		
		labels = {
			'name': _('項目'),

		}