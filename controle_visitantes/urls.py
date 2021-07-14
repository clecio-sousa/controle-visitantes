from django.contrib import admin
from django.urls import path
from usuarios.views import index
from visitantes.views import registrar_visitante #importando a funcao registrar-visitante na VIEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "",
        index,
        name="index",
    ),
    path('registrar-visitante/', #String que representa a URL no navegador
         registrar_visitante,    # funcao da VIEW que deve ser retornada
         name="registrar_visitante")# mesmo nome da VIEW
]
