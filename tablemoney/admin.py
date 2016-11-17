from django.contrib import admin

# Register your models here.

from .models import TableMoney, Month

class TableMoneyInline(admin.TabularInline):
	model = TableMoney


class MonthAdmin(admin.ModelAdmin):
	inlines = [TableMoneyInline, ]
	list_display = ('__str__', 'year', 'month_total')

class TableMoneyAdmin(admin.ModelAdmin):
	list_display = ('month','__str__', 'totle_price')


admin.site.register(TableMoney, TableMoneyAdmin)
admin.site.register(Month, MonthAdmin)
