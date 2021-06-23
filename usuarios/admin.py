from django.contrib import admin
from usuarios.models import Usuario
# Register your models here.

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('id', 'email')
admin.site.register(Usuario, ListandoUsuarios)
