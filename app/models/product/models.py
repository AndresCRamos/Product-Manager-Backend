from django.db import models
from view_table.models import ViewTable
from ..supplier.models import Supplier


class Product(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    sale_value = models.DecimalField(max_digits=10, decimal_places=2)
    no_VAT_value = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_value = models.DecimalField(max_digits=20, decimal_places=2)
    min_quantity = models.IntegerField()
    max_quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)


class ProductSupplier(ViewTable):
    product_name = models.CharField(max_length=100)
    product_quantity = models.BigIntegerField()
    supplier_nit = models.BigIntegerField()
    supplier_name = models.CharField(max_length=100)

    @classmethod
    def get_query(cls):
        sql = "select " +\
              "pp.id as id, " \
              "pp.name as product_name, " \
              "pp.quantity as product_quantity, " \
              "ss.id as supplier_id, " \
              "ss.nit as supplier_nit, " \
              "ss.name as supplier_name " \
              "from product_product pp " \
              "join supplier_supplier ss " \
              "ON pp.supplier_id = ss.id"
        return sql
