from re import search
from django.contrib import admin
from django.db.models import fields
from core.erp.models import *
from core.user.models import User

from import_export import resources


# Register your models here.

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('names', 'rut', 'email', 'phone', 'city')
    search_fields = ('names', 'rut', 'email', 'phone', 'city')
    list_per_page = 10
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ('name', 'desc')
    list_per_page = 10

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('names', 'dni', 'commercial_business', 'phone', 'email', 'address', 'city')
    search_fields = ('names', 'dni', 'commercial_business', 'phone', 'email', 'address', 'city')
    list_per_page = 10

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat', 'proveedor', 'marca', 'image', 'stock', 'preciocompra', 'pvp')
    search_fields = ('name', 'stock', 'preciocompra', 'precioventa')
    list_per_page = 10

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('cli', 'date_joined', 'subtotal', 'iva', 'total')
    search_fields = ('date_joined', 'subtotal', 'iva', 'total')
    list_per_page = 10

@admin.register(DetSale)
class DetSaleAdmin(admin.ModelAdmin):
    list_display = ('sale', 'prod', 'price', 'cant', 'subtotal')
    search_fields = ('sale', 'prod', 'price', 'cant', 'subtotal')
    list_per_page = 10

#@admin.register(Compra)
#class CompraAdmin(admin.ModelAdmin):
#    list_display = ('proveedor', 'date_joined', 'subtotal', 'total')
#    search_fields = ('date_joined', 'subtotal', 'total')
#    list_per_page = 10

#@admin.register(DetCompra)
#class DetCompraAdmin(admin.ModelAdmin):
#    list_display = ('compra', 'prod', 'price', 'cant', 'subtotal')
#    search_fields = ('compra', 'prod', 'price', 'cant', 'subtotal')
#    list_per_page = 10
