from django import forms
from django.forms import fields
from django.forms.models import ModelForm #importando FORMS
from visitantes.models import Visitante #criando FORM a partir de MODELS (from <NOME_DA_APP>.models import NOME_DA_CLASSE) 

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = "__all__" #representa todos os campos