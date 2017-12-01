from django import forms
from .models import Funcionario, Venda
from django.contrib.auth.models import User

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = "__all__"

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class VendaFuncionarioForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ('operador',)
