from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fiels = ['nome', 'email','cpf',]
        widgets = {
            'nome':forms.TextInput(attrs={'placerolder':'Informe o nome do cliente'}),
            'email':forms.TextInput(attrs={'placeholder':'Informe o email do cliente'}),
            'cpf':forms.TextInput(attrs={'placerolder':'Informe o cpf do cliente'}),



        }