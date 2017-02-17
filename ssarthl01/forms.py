from django import forms
from django.contrib.auth import get_user_model
from django.contrib import messages


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label="帳號")
    password = forms.CharField(label="密碼", widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user_obj = User.objects.filter(username=username).first()
        if not user_obj:
            raise forms.ValidationError('帳號或密碼錯誤')
        else:
            if not user_obj.check_password(password):
                raise forms.ValidationError('帳號或密碼錯誤')
        return super(UserLoginForm, self).clean(*args, **kwargs)
