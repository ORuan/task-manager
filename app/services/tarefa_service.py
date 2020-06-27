from ..models import Tarefa

def listar_tarefas(id_user):
    todas_do_user = Tarefa.objects.filter(usuario=id_user).all()
    return todas_do_user

def listar_tarefas_id(id,id_user):
    todas_do_user_id = Tarefa.objects.filter(usuario=id_user).all()
    return todas_do_user_id.get(id=id)

def deletar_tarefa(tarefa,id_user):
    todas_do_user_del = Tarefa.objects.filter(usuario=id_user).all()
    
    return tarefa.delete()
    



