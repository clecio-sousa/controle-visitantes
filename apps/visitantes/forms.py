from django import forms
from django.contrib.messages.api import error
from django.forms import fields
from django.forms.models import ModelForm #importando FORMS
from visitantes.models import Visitante #criando FORM a partir de MODELS (from <NOME_DA_APP>.models import NOME_DA_CLASSE) 

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = "__all__" #representa todos os campos
        
        
        # INICIO DAS MENSAGENS DE ERRO NO FORMULARIO
        error_messages = {
            "nome_completo" :{
                "required": " O nome completo é obrigatório"
            },
             "cpf" :{
                "required": " O CPF é obrigatório"
            },
            "data_nascimento" :{
                "required": " A data de nascimento é obrigatória",
                "invalid": "Informe um formato válido para a data de nascimento(DD/MM/AAAA)"
            },
             "numero_casa" :{
                "required": "Informe o número da casa a ser visitada"
            }
            
        }
        #FIM DAS MENSAGENS DE ERRO NO FORMULARIO
class AutorizaVisitanteForm(forms.ModelForm):
    
    morador_responsavel = forms.CharField(required=True)
    class Meta:
        model = Visitante
        fields =[
            "morador_responsavel"            
        ]
        error_messages ={
            "morador_responsavel": {
                "required":"Por favor, informe o nome do morador responsável por autorizar a entrada do visitante"
            }
        }
        
        
        """" 
        CAMPOS SELECIONADOS
        
        fields = (
            "nome_completo", "cpf","data_nascimento",
            "numero_casa", "placa_veiculo"
        )
        """