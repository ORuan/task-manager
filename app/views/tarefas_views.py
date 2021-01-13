from django.shortcuts import render,redirect
from ..forms import TarefaForm
from django.contrib.auth.models import User
from ..services import tarefa_service
from django.contrib.auth.decorators import login_required
from ..models import Tarefa


def index(request):
    return render(request, 'index.html')


def listar_publicas(request):
    tarefas = Tarefa.objects.filter(public=True)
    return render(request, 'tarefas/tarefas_publicas.html', {'tarefas': tarefas})


@login_required
def listar_tarefas(request):
    usuario_logado  = request.user.id
    tarefas = tarefa_service.listar_tarefas(usuario_logado)
    return render(request, 'tarefas/listar_tarefas.html',{'tarefas':tarefas})

@login_required
def cadastrar_tarefas(request):
    if request.method == 'POST':
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():

            form_tarefa_save = form_tarefa.save(commit=False)
            user = User.objects.get(id=request.user.id)
            form_tarefa_save.usuario = user
            form_tarefa_save.save()
            return redirect('app:listar_tarefas')

    else:
        form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html',{'form_tarefa':form_tarefa})

@login_required
def editar_tarefas(request, id):
    usuario_logado  = request.user.id
    tarefa_especifica = tarefa_service.listar_tarefas_id(id,usuario_logado)
    form_tarefa = TarefaForm(request.POST or None, instance=tarefa_especifica)
    if request.method == 'POST':
        if form_tarefa.is_valid():
            form_tarefa.save()
            return redirect('app:listar_tarefas')
        else:
            redirect('app:editar_tarefas')
    return render(request, 'tarefas/form_tarefa.html', {'form_tarefa':form_tarefa})

@login_required
def remover_tarefas(request, id):
    usuario_logado  = request.user.id
    tarefa_especifica = tarefa_service.listar_tarefas_id(id,usuario_logado)
    if request.method == 'POST':
        tarefa_service.deletar_tarefa(tarefa_especifica,usuario_logado)
        return redirect ('app:listar_tarefas')
    return render(request, 'tarefas/confirma_exclusao.html',{'tarefa':tarefa_especifica })
