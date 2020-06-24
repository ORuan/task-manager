from django.shortcuts import render,redirect
from ..forms import TarefaForm
from ..services import tarefa_service
from django.contrib.auth.decorators import login_required

@login_required
def listar_tarefas(request):
    

    tarefas = tarefa_service.listar_tarefas()
    return render(request, 'tarefas/listar_tarefas.html',{'tarefas':tarefas})

@login_required
def cadastrar_tarefas(request):
    if request.method == 'POST':
        form_tarefa = TarefaForm(request.POST)
        form_tarefa.usuario = request.user
        if form_tarefa.is_valid():
            
            form_tarefa.save()
            return redirect('listar_tarefas')

    else:
        form_tarefa = TarefaForm()


    return render(request, 'tarefas/form_tarefa.html',{'form_tarefa':form_tarefa})

@login_required
def editar_tarefas(request, id):
    print(request.user.id)

    tarefa_especifica = tarefa_service.listar_tarefas_id(id)
    form_tarefa = TarefaForm(request.POST or None, instance=tarefa_especifica)
    if request.method == 'POST':

        if form_tarefa.is_valid():
            form_tarefa.save()
            return redirect('listar_tarefas')
        else:
            redirect('editar_tarefas')
    
    return render(request, 'tarefas/form_tarefa.html', {'form_tarefa':form_tarefa})


@login_required
def remover_tarefas(request, id):
    tarefa_especifica = tarefa_service.listar_tarefas_id(id)

    if request.method == 'POST':
        tarefa_service.deletar_tarefa(tarefa_especifica)
        return redirect ('listar_tarefas') 
    
    return render(request, 'tarefas/confirma_exclusao.html',{'tarefa':tarefa_especifica })
