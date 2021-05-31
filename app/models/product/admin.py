from django.contrib import admin
from .models import Product, ProductSupplier


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'supplier_nit', 'supplier_name')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSupplier, ProductViewAdmin)
