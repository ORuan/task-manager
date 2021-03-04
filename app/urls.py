from django.contrib import admin
from django.urls import path
from .views.tarefas_views import *
from .views.usuarios_views import *


urlpatternsuser = [
    path('cadastrar-usuario/', cadastrar_usuario, name="cadastrar_usuario"),
    path('logar-usuario/', logar_usuario, name="logar_usuario"),
    path('deslogar-usuario/', deslogar_usuario, name="deslogar_usuario"),
]

urlpatterns = [
    path('listar/', listar_tarefas, name="listar_tarefas"),
    path('publicas/', listar_publicas, name="tarefas_publicas"),
    path('cadastrar/', cadastrar_tarefas, name="cadastrar_tarefas"),
    path('editar/<int:id>/', editar_tarefas, name="editar_tarefas"),
    path('remover/<int:id>/', remover_tarefas, name="remover_tarefas"),
    
] 
urlpatterns += urlpatternsuser
