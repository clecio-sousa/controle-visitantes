from django.contrib import admin
from porteiros.models import Porteiro # importando a classe porteiro de models>> nome_do_app.models import nome_da_classe

# Register your models here.
class ListandoPorteiros(admin.ModelAdmin):
    list_display = ('id', 'nome_completo')
    list_display_links = ('id', 'nome_completo')
admin.site.register(Porteiro, ListandoPorteiros)

