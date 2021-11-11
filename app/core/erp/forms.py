from datetime import datetime
from django.forms import ModelForm
from django.forms import *
from core.erp.models import *

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True


    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class SubCategoryForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Subcategory
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre Cargo',
                }
            ),
            'cat': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
            }),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ProveedorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs = {
                    'placeholder': 'Empresa Proveedora'
                }
            ),
            'rut': TextInput(
                attrs = {
                    'placeholder': 'RUT'
                }
            ),
            'phone': TextInput(
                attrs = {
                    'placeholder': 'Contacto'
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Dirección',
                }
            ),
            'city': TextInput(
                attrs={
                    'placeholder': 'Ciudad',
                }
            ),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class MarcaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Nombre Marca',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'cat': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'subcat': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'proveedor': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width:100%',
            }),
            'marca': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width:100%',
            }),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder': 'Empresa',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'RUT (Use puntos y guión  - EJ: 11.111.111-1)',
                }
            ),
            'commercial_business': TextInput(
                attrs={
                    'placeholder': 'Giro Comercial',
                }
            ),
            'phone': TextInput(
                attrs={
                    'placeholder': 'Contacto Telefonico',
                },
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Dirección',
                }
            ),
            'city': TextInput(
                attrs={
                    'placeholder': 'Ciudad',
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TestForm(Form):
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    products = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))
    search = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(attrs={
                'class': 'custom-select select2',
            }),
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'formapago': Select(
                attrs={
                    'class': 'form-control select2',
                    'style': 'width:100%'
            }),
            'iva': TextInput(attrs={
                'class': 'form-control',
                'readonly': True
            }),
            'subtotal': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }

class GroupPermissionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Group
        fields = 'name', 'permissions'
        widgets = {
            'name': TextInput(
                attrs = {
                    'placeholder': 'Nombre Grupo',
                }
            ),
            'permissions': SelectMultiple(
                attrs = {
                    'rows': 10
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class DepartmentForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre Departamento',
                }
            ),
        }
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class CargoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    
    class Meta:
        model = Cargos
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre Cargo',
                }
            ),
            'department': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
            }),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TrabajadorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Trabajador
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'RUT (Use puntos y guión  - EJ: 11.111.111-1)',
                }
            ),
            'phone': TextInput(
                attrs={
                    'placeholder': 'Contacto Telefonico',
                },
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Dirección',
                }
            ),
            'city': TextInput(
                attrs={
                    'placeholder': 'Ciudad',
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'department': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'cargo': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data