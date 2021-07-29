from django.shortcuts import render
from visitantes.models import Visitante
from django.utils import timezone
from django.contrib.auth.decorators import login_required #somente users autenticados terao acesso ao dashboard
# Create your views here.

@login_required #somente users autenticados terao acesso ao dashboard
def index(request):
    
    todos_visitantes = Visitante.objects.order_by(  
        "-horario_chegada" #filtra os registrantes mais recentes no topo
    )
    
    visitantes_aguardando = todos_visitantes.filter(
        status = "AGUARDANDO"
    )
    visitantes_em_visita = todos_visitantes.filter(
        status = "EM_VISITA"
    )
    visitantes_finalizado = todos_visitantes.filter(
        status = "FINALIZADO"
    )
    
    hora_atual = timezone.now()
    mes_atual = hora_atual.month
    
    visitantes_mes = todos_visitantes.filter(
        horario_chegada__month = mes_atual #uso do FIELD LOOKUPS
    )
    context={
        "nome_pagina" : "Inicio da dashboard",
        "todos_visitantes" : todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count(),
        "visitantes_em_visita": visitantes_em_visita.count(),
        "visitantes_finalizado": visitantes_finalizado.count(),
        "visitantes_mes": visitantes_mes.count()

        #count - registra a quantidade de visitantes em cada status
        
    }    
    return render(request, "index.html", context)



