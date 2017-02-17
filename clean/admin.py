from django.contrib import admin
from .models import CleanMonth

# Register your models here.

class CleanMonthAdmin(admin.ModelAdmin):
	list_display = ('__str__', )


admin.site.register(CleanMonth, CleanMonthAdmin)