from django import forms
from .models import Funcionario, Venda

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = "__all__"

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = "__all__"
