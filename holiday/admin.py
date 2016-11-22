from django.contrib import admin

from .models import HolidayMonth, Date, Holiday
# Register your models here.


class HolidayInline(admin.TabularInline):
	model = Holiday

class HolidayMonthAdmin(admin.ModelAdmin):
	inlines = [HolidayInline, ]
	list_display = ('__str__', 'year')

class HolidayAdmin(admin.ModelAdmin):
	list_display = ('month','year' ,'__str__', )

class DateAdmin(admin.ModelAdmin):
	list_display = ('__str__', )


admin.site.register(HolidayMonth, HolidayMonthAdmin)
admin.site.register(Holiday, HolidayAdmin)
admin.site.register(Date, DateAdmin)