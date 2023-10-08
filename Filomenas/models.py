from django.db import models
from django.utils.translation import gettext_lazy as _
from Filomenas.constants import (MAX_CHAR_FIELD_NAME_LENGTH,MEDIUM_CHAR_FIELD_NAME_LENGTH,SMALL_CHAR_FIELD_NAME_LENGTH)
from main.models import BaseModel



class Cadastro_cliente(BaseModel):

    Nome = models.CharField(
        verbose_name=_("Nome"), max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH,
    )
    
    Cpf = models.CharField(
        verbose_name=_("Cpf"), max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH,
    )
    
    Endereco = models.CharField(
        verbose_name=_("Endereço"), max_length=MEDIUM_CHAR_FIELD_NAME_LENGTH,
    )
    
    Telefone = models.CharField(
        verbose_name=_("Telefone"), max_length=SMALL_CHAR_FIELD_NAME_LENGTH,
    )
    
    email = models.CharField(
        verbose_name=_("email"), max_length=SMALL_CHAR_FIELD_NAME_LENGTH,
    )
    
    profissao = models.CharField(
        verbose_name=_("Profissão"), max_length=SMALL_CHAR_FIELD_NAME_LENGTH,
    )
    
    Idade = models.DecimalField(
        verbose_name=_("Idade"),
        decimal_places=2,
        max_digits=3
    )
    

    class Meta:
        verbose_name = _("Filomena")
        verbose_name_plural = _("Filomenas")

    # def __str__(self):
    #     return f"{self.pk} | {self.localizacao} | {self.valor}"

class Cadastro_filomena(BaseModel):
    nome = models.CharField(max_length=150)
    email = models.CharField