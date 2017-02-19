from django.contrib import admin

from .models import HolidayMonth, Date, Holiday, HolidayFromDocx, HolidayMonthFromDocx
# Register your models here.


class HolidayInline(admin.TabularInline):
	model = Holiday

class HolidayMonthAdmin(admin.ModelAdmin):
	inlines = [HolidayInline, ]
	list_display = ('__str__', 'year')

class HolidayAdmin(admin.ModelAdmin):
	list_display = ('month','year' ,'__str__', )

class HolidayFromDocxAdmin(admin.ModelAdmin):
	list_display = ('month','year' ,'__str__', )

class HolidayMonthFromDocxAdmin(admin.ModelAdmin):
	list_display = ('month','year' ,'__str__', )

class DateAdmin(admin.ModelAdmin):
	list_display = ('__str__', )


admin.site.register(HolidayMonth, HolidayMonthAdmin)
admin.site.register(Holiday, HolidayAdmin)
admin.site.register(Date, DateAdmin)
admin.site.register(HolidayFromDocx, HolidayFromDocxAdmin)
admin.site.register(HolidayMonthFromDocx, HolidayMonthFromDocxAdmin)
