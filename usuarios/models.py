from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin, #Essas 3 classes permitem criar um modelo personalizado de usuário
)

# Create your models here.
class UsuarioManager(BaseUserManager): #sub-classe de BaseUserManager
    def create_user(self, email, password=None):
        usuario = self.model(
            email = self.normalize_email(email) # metodo que evita que o email seja salvo fora do padrao
                    
        )
        
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()
        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        
        usuario.set_password = True

        usuario.save()

        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):
    
    
    
    email = models.EmailField(
        verbose_name='E-mail do usuário',
        max_length=200,
        unique=True, # indica que nao pode existir 2 usuarios com o mesmo email
    )
    
    is_active = models.BooleanField(
        verbose_name='Usuário está ativo',
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name='Usuário é da equipe de desenvolvimento',
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name='Usuário é um superusuário',
        default=False,
    )

    USERNAME_FIELD = "email" # informa qual atributo da classe deve ser usado como autenticacao

    objects = UsuarioManager()


    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario" # Nome da tabela no BD

        def __str__(self):
            return self.nome_completo




