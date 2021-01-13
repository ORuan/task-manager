from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:listar_tarefas')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {'form':form})

def logar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        paswd = request.POST['password']
        usuario = authenticate(request, username=username, password=paswd)
        if usuario is not None:
            login(request, usuario)
            return redirect('app:listar_tarefas')
        else:
            messages.error(request, 'As credências estão incorretas!')
            return redirect('app:logar_usuario')


    login_form = AuthenticationForm()
    return render(request, 'usuarios/form_login.html', {'form_login':login_form})

def deslogar_usuario(request):
    logout(request)
    return redirect('app:logar_usuario')