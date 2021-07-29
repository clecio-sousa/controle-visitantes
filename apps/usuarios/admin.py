from django.contrib import admin
from usuarios.models import Usuario
# Register your models here.

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('id', 'username','nome_completo')
    list_display_links = ['username']
admin.site.register(Usuario, ListandoUsuarios)
