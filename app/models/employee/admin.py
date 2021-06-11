from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id_card', 'user', 'type')


admin.site.register(Employee, EmployeeAdmin)
