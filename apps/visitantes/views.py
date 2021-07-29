from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #somente users autenticados terao acesso ao dashboard
from visitantes.models import Visitante
from visitantes.forms import VisitanteForm, AutorizaVisitanteForm #importando VISITANTES FORMS de forms
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseNotAllowed

# Create your views here.

#VIEW P/FAZER P CADASTRO DO VISITANTE

@login_required
def registrar_visitante(request):
    
    form = VisitanteForm()
    
    if request.method == "POST":
        form = VisitanteForm(request.POST)
        
        if form.is_valid():
            visitante = form.save(commit=False)  # variável visitante recebe o resultado do método SAVE 
                                                 #COMMIT retorna um visitante que ainda nao esta salvo no BD 
                                                             
            visitante.registrado_por = request.user.porteiro #retorna o porteiro que está logado
            visitante.save() # SALVA EM DEFINITIVO O VISITANTE NO BD
            messages.success(
                request,
                "Visitante registrado com sucesso!"
            )
            
            return redirect("index") #redireciona o usuario p/ a pagina index após efetuar o cadastro                                                     
    
    context = {
        "nome_pagina" : "Registrar Visitante",
        "form" : form        
    }    
    return render(request, "registrar_visitante.html", context)


#VIEW P/BUSCAR INFORMACOES DO VISITANTE
@login_required
def informacoes_visitante(request, id):
    
    visitante = get_object_or_404(
        Visitante,
        id=id
    )
    
    form = AutorizaVisitanteForm()
    
    if request.method == "POST":
        form = AutorizaVisitanteForm(
            request.POST,
            instance=visitante
        )
        
        if form.is_valid():
            
            visitante = form.save(commit=False)
            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = timezone.now()
            visitante.save()
            
            messages.success(
                request, "Entrada de visitante autorizada" 
            )
            
            return redirect ("index")
    
    context = {
        "visitante": visitante,
        "nome_pagina": "Informações do visitante",
        "form": form
    }
    return render(request, "informacoes_visitante.html", context)

@login_required
def finalizar_visita(request, id):
    if request.method == "POST":
        visitante = get_object_or_404(
            Visitante,
            id=id
        )
        
        visitante.status = "FINALIZADO"
        visitante.horario_saida = timezone.now()
        visitante.save()
        
        messages.success(
            request,
            "Visita finalizada com sucesso"
        )
        return redirect("index")
    
    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Método não permitido"
        )