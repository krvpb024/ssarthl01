from django.contrib import admin

# Register your models here.

from .models import UserProfile, Payee



class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'rank')
	class Meta:
		model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Payee)