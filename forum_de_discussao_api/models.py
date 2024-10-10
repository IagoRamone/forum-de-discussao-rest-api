from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modelo de banco de dados para os usuários do sistema"""
    email = models.EmailField(max_lenght=255, unique=True)
    name = models.CharField(max_lenght=255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name']

     def get_full_name(self):
         """Pega o nome completo da pessoa """
        return self.email

    def get_short_name(self):
        """Pega o menor nome """
        return self.name

def __str__(self):
    """Retorna o email do usuario"""
    return self.email
