from django.contrib import admin
from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'nit', 'name', )


admin.site.register(Supplier, SupplierAdmin)
