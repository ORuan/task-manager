from django.contrib import admin
from django.urls import path, include
from app.tarefas_views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', include('app.urls')),
    path('', index, name="index"),

]
