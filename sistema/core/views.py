from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import FuncionarioForm, VendaForm
from .models import Funcionario, Venda, Comissao

# Create your views here.

def home(request):
    #form = FuncionarioForm()
    return render(request, "base.html", {})

def cadastra_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_funcionario')
        else:
            print(form.errors)
    else:
        form = FuncionarioForm()
    return render(request, "cadastra_funcionario.html", {'form' : form})

def consulta_funcionario(request):
    funcionario = Funcionario.objects.all()
    return render(request, "consulta_funcionario.html", {"funcionario": funcionario})

def deleta_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id).delete()
    return redirect('consulta_funcionario')

def edita_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('consulta_funcionario')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'cadastra_funcionario.html', {"form":form})

def cadastra_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_venda')
        else:
            print(form.errors)
    else:
        form = VendaForm()
    return render(request, "cadastra_venda.html", {'form' : form})

def consulta_venda(request):
    venda = Venda.objects.all()
    return render(request, "consulta_venda.html", {"venda": venda})

def edita_venda(request, id):
    venda = get_object_or_404(Venda, id=id)
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('consulta_venda')
    else:
        form = VendaForm(instance=venda)
    return render(request, 'cadastra_venda.html', {"form":form})

def deleta_venda(request, id):
    venda = Venda.objects.get(id=id).delete()
    return redirect('consulta_venda')
