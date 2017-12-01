from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Funcionario(models.Model):
    CATEGORIAS=(
        ("AGT", "Agente de Crédito"),
        ("ADM", "Auxiliar Administrativo")
    )
    chave = models.CharField(max_length=9, verbose_name="Chave")
    categoria = models.CharField(max_length=40, choices=CATEGORIAS, verbose_name="Categoria")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.CharField(max_length=100, verbose_name="E-mail")

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.chave

class Venda(models.Model):
    ESTADOS = (
        ("AG", "Aguardando"),
        ("CN", "Cancelado"),
        ("LB", "Liberado")
    )
    operacao = models.CharField(max_length=50, verbose_name="Operação")
    produto = models.ForeignKey("Produto", verbose_name="Produto")
    data = models.DateField(default=date.today)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    troco = models.DecimalField(max_digits=12, decimal_places=2)
    prazo = models.IntegerField(verbose_name="Prazo")
    estado = models.CharField(max_length=20, choices=ESTADOS, verbose_name="Estado")
    agencia = models.IntegerField(default="0000", verbose_name="Agência")
    loja = models.IntegerField(default="0000", verbose_name="Loja")
    operador = models.ForeignKey('Funcionario', verbose_name="Vendedor")
    #user = models.ForeignKey(User)

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"


    def __str__(self):
        return self.operacao

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    tipo = models.CharField(max_length=100, verbose_name="Tipo")
    linha = models.IntegerField(default="0000", verbose_name="Linha")
    convenio = models.CharField(max_length=100, verbose_name="Convênio")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome

class Comissao(models.Model):

    class Meta:
        verbose_name = "Comissão"
        verbose_name_plural = "Comissões"

    pass
