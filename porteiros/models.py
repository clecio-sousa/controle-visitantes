from django.db import models

# Create your models here.
class Porteiro(models.Model):
    
    usuario = models.OneToOneField(
        "usuarios.Usuario", #aplicativo.Nome_da_classe
        verbose_name="Usuário",
        on_delete=models.PROTECT #impede que o registro do objeto seja excluido
    )    
    
    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=194,
    )
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )
    telefone = models.CharField(
        verbose_name="Telefone de contato",
        max_length=11
    )
    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False, #atualizar o valor sempre que atualizar as informacoes do objeto(porteiro)
        auto_now_add=False #utilizar data atual como registro no BD
    )
    
    
    class Meta: #classes e metodos que acompanha todos os modelos do django
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"
    
    def __str__(self):
        return self.nome_completo
    
        
        