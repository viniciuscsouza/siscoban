from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserForm

# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Usuário Criado')
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form': form})
