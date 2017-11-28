from django.contrib import admin
from .models import Funcionario, Venda, Produto, Comissao

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(Comissao)
