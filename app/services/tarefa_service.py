from ..models import Tarefa

def listar_tarefas():
    return Tarefa.objects.all()

def listar_tarefas_id(id):
    return Tarefa.objects.get(id=id)

def deletar_tarefa(tarefa):
    return tarefa.delete()


