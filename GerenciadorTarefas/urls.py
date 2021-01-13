from django.contrib import admin
from django.urls import path, include
from app.views.tarefas_views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', include(('app.urls','app'), namespace='app')),
    path('home/', index, name="home"),
    path('', index, name="index"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
