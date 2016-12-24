from django import forms
from .models import ZhuDiTable

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
