from django.shortcuts import render, redirect, get_object_or_404
from visitantes.models import Visitante
from visitantes.forms import VisitanteForm #importando VISITANTES FORMS de forms
from django.contrib import messages

# Create your views here.

#VIEW P/FAZER P CADASTRO DO VISITANTE

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
def informacoes_visitante(request, id):
    
    visitante = get_object_or_404(
        Visitante,
        id=id
    )
    
    context = {
        "visitante": visitante,
        "nome_pagina": "Informações do visitante,"
    }
    return render(request, "informacoes_visitante.html", context)