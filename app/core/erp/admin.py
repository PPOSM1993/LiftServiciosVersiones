from django.contrib import admin
from django.db.models import fields
from core.erp.models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class GategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('name', 'desc')
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields =['name']
    list_display = ('name', 'desc')
    resource_class = GategoryResource
    
class MarcaResource(resources.ModelResource):
    class Meta:
        model = Marca
        fields = ('name')

class MacarAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    resource_class = MarcaResource




class FormaPagosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Proveedor)
admin.site.register(Marca, MacarAdmin)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Department)


