from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import FuncionarioForm, VendaForm, UserForm
from .models import Funcionario, Venda, Comissao
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def home(request):
    #form = FuncionarioForm()
    return render(request, "base.html", {})

@login_required
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

@login_required
def consulta_funcionario(request):
    funcionario = Funcionario.objects.all()
    return render(request, "consulta_funcionario.html", {"funcionario": funcionario})

@login_required
def deleta_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id).delete()
    return redirect('consulta_funcionario')

@login_required
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

@login_required
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

@login_required
def consulta_venda(request):
    venda = Venda.objects.all()
    return render(request, "consulta_venda.html", {"venda": venda})

@login_required
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

@login_required
def deleta_venda(request, id):
    venda = Venda.objects.get(id=id).delete()
    return redirect('consulta_venda')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('user_login')
        else:
            messages.error(request, 'Não foi possível cadastrar o usuário')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Usuário ou senha inválido.')
    return render(request, 'user_login.html', {})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('change_password')
        else:
            messages.error(request, 'Não foi possível alterar a sua senha.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')
