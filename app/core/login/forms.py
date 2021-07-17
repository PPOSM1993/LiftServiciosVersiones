from django import forms
from core.user.models import User

class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nombre de Usuario',
        'class': 'form-control',
        'autocomplete': 'off'
    }))
    
    def clean(self):
        cleaned = super().clean()
        if not User.objects.filter(username=cleaned['username']).exists():
            self._errors['error'] = self._errors.get('error', self.error_class())
            self._errors['error'].append('Usuario no Existente')
            #raise forms.ValidationError('Usuario no Existente')
        return cleaned
    
    def get_user(self):
        username = self.cleaned_data.get('username')
        return User.objects.get(username=username)


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Nueva Contraseña',
        'class': 'form-control',
        'autocomplete': 'off'
    }))
    
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar nueva Contraseña',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    def clean(self):
        cleaned = super().clean()
        password = cleaned['password']
        confirmPassword = cleaned['confirmPassword']
        if password != confirmPassword:

            raise forms.ValidationError('Las contraseñas deben ser Identicas')
        return cleaned
