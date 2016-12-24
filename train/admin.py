from django.contrib import admin

# Register your models here.

from .models import ZhuDi, ZuXun, ZhuDiTable, ZuXunTable


class ZhuDiAdmin(admin.ModelAdmin):
	list_display = ('__str__',)

class ZuXunAdmin(admin.ModelAdmin):
	list_display = ('__str__',)

class ZhuDiTableAdmin(admin.ModelAdmin):
	list_display = ('date','__str__',)

class ZuXunTableAdmin(admin.ModelAdmin):
	list_display = ('date','__str__',)


admin.site.register(ZhuDi, ZhuDiAdmin)
admin.site.register(ZuXun, ZuXunAdmin)
admin.site.register(ZhuDiTable, ZhuDiTableAdmin)
admin.site.register(ZuXunTable, ZuXunTableAdmin)
