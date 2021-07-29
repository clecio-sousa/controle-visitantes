from django.contrib import admin
from django.urls import path
from dashboard.views import index
from visitantes.views import registrar_visitante, informacoes_visitante, finalizar_visita #importando a funcao registrar-visitante na VIEW
from django.contrib.auth import views as auth_views # URL de login e logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "",
        index,
        name="index",
    ),
    
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login"
        
    ),
    
    path(
      "logout/"  ,
      auth_views.LogoutView.as_view(
          template_name="logout.html"
      ),
      name="logout"
    ),
    
    path(
        "registrar-visitante/", #String que representa a URL no navegador
         registrar_visitante,    # funcao da VIEW que deve ser retornada
         name="registrar_visitante",
         ),# mesmo nome da VIEW
    
    path(
        "informacao-visitante/<int:id>/",
        informacoes_visitante,
        name="informacoes_visitante"
         ),
    
    path("informacao-visitante/<int:id>/finalizar-visita",
         finalizar_visita,
         name="finalizar_visita"        
    )
]
