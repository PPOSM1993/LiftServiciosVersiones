from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser

from config.settings import MEDIA_URL, STATIC_URL
from core.models import BaseModel

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Subcategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoría')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        return item

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'
        ordering = ['id']

class Proveedor(models.Model):
    
    name = models.CharField(max_length=150, verbose_name='Empresa Proveedora', unique=True)
    rut_regex = RegexValidator(
        regex=r'^0*(\d{1,3}(\.?\d{3})*)\-?([\dkK])$', message="Formato de Rut Incorrecto.")
    rut = models.CharField(
        validators=[rut_regex], max_length=12, unique=True, verbose_name='RUT')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número de telefono debe tener el siguiente: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True, verbose_name="Telefono") # validators should be a list
    email = models.EmailField(
        max_length=150, null=True, blank=True, verbose_name='Email', unique=True)
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    city = models.CharField(max_length=150, null=True, blank=True, verbose_name='Ciudad')
    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} / {}'.format(self.name, self.rut)
    
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']

class Marca(models.Model):
    name = models.CharField(
        max_length=150, verbose_name='Nombre Marca', unique=True)
    
    def __str__(self):
        return self.name
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['id']

class Product(models.Model):
    
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoría')
    subcat = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name='Subcategoría')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, verbose_name='Proveedor')
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, verbose_name='Marca')
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    stock = models.IntegerField(default=0, verbose_name='Stock')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        item['proveedor'] = self.proveedor.toJSON()
        item['marca'] = self.marca.toJSON()
        item['image'] = self.get_image()
        item['pvp'] = format(self.pvp, '.2f')
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Client(models.Model): 
    names = models.CharField(max_length=150, verbose_name='Empresa', unique=True)
    dni_regex = RegexValidator(
        regex=r'^0*(\d{1,3}(\.?\d{3})*)\-?([\dkK])$', message="Formato de Rut Incorrecto.")
    dni = models.CharField(
        validators=[dni_regex], max_length=12, unique=True, verbose_name='RUT')

    commercial_business = models.CharField(max_length=150, null=True, blank=True, verbose_name='Giro Comercial')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número de telefono debe tener el siguiente: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True, verbose_name="Telefono") # validators should be a list
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    city = models.CharField(max_length=150, null=True, blank=True, verbose_name='Ciudad')
    email = models.EmailField(max_length=150, null=True, blank=True, verbose_name='Email', unique=True)
    
    def __str__(self):
        return self.get_full_name()
    
    def get_full_name(self):
        return '{} / {}'.format(self.names, self.dni)

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(
        default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    def toJSON(self):
        item = model_to_dict(self)
        item['cli'] = self.cli.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['det'] = [i.toJSON() for i in self.detsale_set.all()]
        return item

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id'] 

class DetSale(models.Model):
    
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=0)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(
        default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    def toJSON(self):
        item = model_to_dict(self, exclude=['sale'])
        item['prod'] = self.prod.toJSON()
        item['price'] = format(self.price, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']

class Group(Group, models.Model):

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def toJSON(self):
        item = model_to_dict(
            self, exclude=['groups', 'permissions'])
        return item

class Department(models.Model):
    
    name = models.CharField(max_length=100, unique=True, verbose_name="Departamento")
    
    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['id']

class Cargos(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Cargo")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name='Departamento')
    
    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['department'] = self.department.toJSON()
        return item

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ['id']

class Trabajador(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, unique=True, verbose_name="Apellido")
    dni_regex = RegexValidator(
        regex=r'^0*(\d{1,3}(\.?\d{3})*)\-?([\dkK])$', message="Formato de Rut Incorrecto.")
    dni = models.CharField(
        validators=[dni_regex], max_length=12, unique=True, verbose_name='RUT')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número de telefono debe tener el siguiente: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True, verbose_name="Telefono") # validators should be a list
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    city = models.CharField(max_length=150, null=True, blank=True, verbose_name='Ciudad')
    email = models.EmailField(max_length=150, null=True, blank=True, verbose_name='Email', unique=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name='Departamento')
    cargo = models.ForeignKey(Cargos, on_delete=models.PROTECT, verbose_name='Cargo')
    

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['department'] = self.department.toJSON()
        item['cargo'] = self.cargo.toJSON()
        return item

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id'] 