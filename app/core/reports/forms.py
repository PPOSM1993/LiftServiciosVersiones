from django.forms import *

class ReportForm(Form):
    date_range = CharField(widget=TextInput(attrs={
        'class': 'form-control select2',
        'autocomplete': 'off'
    }))
